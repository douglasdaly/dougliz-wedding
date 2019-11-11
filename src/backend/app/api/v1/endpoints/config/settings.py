# -*- coding: utf-8 -*-
"""
Settings API endpoint.
"""
import typing as tp
from uuid import UUID

from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import Query

from app.api.utils.security import get_current_active_superuser
from app.api.utils.security import get_current_active_user
from app.api.utils.storage import get_uow
from app.crud.core import UnitOfWork
from app.exceptions import APIError
from app.models.user import UserInDB
from app.models.config.setting import DataT
from app.models.config.setting import Setting
from app.models.config.setting import SettingCreate
from app.models.config.setting import SettingInDB
from app.models.config.setting import SettingUpdate


router = APIRouter()


@router.post('/', response_model=Setting)
def create_setting(
    *,
    new_setting: SettingCreate = Body(...),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_superuser)
) -> SettingInDB:
    """Create a new setting.

    Parameters
    ----------
    new_setting : SettingCreate
        The data to use to create the new setting.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current user making the request.

    Returns
    -------
    SettingInDB
        The newly created setting object.

    Raises
    ------
    ObjectExistsError
        If the setting already exists.

    """
    with uow:
        return uow.config.setting.create(new_setting)


@router.get('/', response_model=tp.List[Setting])
def read_settings(
    *,
    skip: tp.Optional[int] = Query(None),
    limit: tp.Optional[int] = Query(None),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_user)
) -> tp.List[SettingInDB]:
    """Gets a list of existing settings.

    Parameters
    ----------
    skip : int, optional
        Number of settings to skip in returned results.
    limit : int, optional
        Number of settings to limit returned results to.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current user making the request.

    Returns
    -------
    List[SettingInDB]
        List of existing settings.

    """
    return uow.config.setting.all(skip=skip, limit=limit)


@router.get('/{name}', response_model=tp.Optional[DataT])
def read_setting_value(
    name: str,
    *,
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_user)
) -> DataT:
    """Gets a single setting value from the given name.

    Parameters
    ----------
    name : str
        The name of the setting to get.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current user making the request.

    Returns
    -------
    Optional[DataT]
        The setting's value requested (or ``None``).

    Raises
    ------
    APIError
        If the setting object with the specified `name` is required to
        be set, but is not.
    ObjectNotFoundError
        If the Setting object with the specified `name` doesn't exist.

    """
    setting = uow.config.setting.get_by_name(name, raise_ex=True)
    if setting.required and setting.value is None:
        raise APIError("Setting value not set")
    return setting.value


@router.get('/id/{id}', response_model=Setting)
def read_setting_id(
    id: UUID,
    *,
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_user)
) -> SettingInDB:
    """Gets a single setting.

    Parameters
    ----------
    id : UUID
        The unique ID of the setting to get.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current user making the request.

    Returns
    -------
    SettingInDB
        The setting requested.

    """
    return uow.config.setting.get(id)


@router.put('/id/{id}', response_model=Setting)
def update_setting_id(
    id: UUID,
    *,
    updated_setting: SettingUpdate = Body(...),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_superuser)
) -> SettingInDB:
    """Updates the specified setting.

    Parameters
    ----------
    id : UUID
        The unique ID of the setting to update.
    updated_setting : SettingUpdate
        The data to update the setting with.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current user making the request.

    Returns
    -------
    SettingInDB
        The updated setting.

    Raises
    ------
    ObjectNotFoundError
        If the Setting object with the specified `id` doesn't exist.

    """
    current = uow.config.setting.get(id)
    with uow:
        return uow.config.setting.update(current, updated_setting)


@router.put('/{name}', response_model=Setting)
def update_setting(
    name: str,
    *,
    value: tp.Optional[DataT] = Body(None),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_superuser)
) -> SettingInDB:
    """Updates the value of a setting.

    Parameters
    ----------
    name : str
        The name of the :obj:`Setting` to update.
    value : Optional[DataT]
        The new value to use for the `name` setting.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current user making the request.

    Returns
    -------
    SettingInDB
        The updated setting.

    Raises
    ------
    ObjectNotFoundError
        If the :obj:`Setting` object with the specified `name` doesn't
        exist.

    """
    current = uow.current.setting.get_by_name(name)
    with uow:
        return uow.config.setting.update_value(current, value)


@router.delete('/id/{id}', response_model=Setting)
def delete_setting_id(
    id: UUID,
    *,
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_superuser)
) -> SettingInDB:
    """Deletes the specified setting.

    Parameters
    ----------
    id : UUID
        The unique ID of the setting to delete.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current user making the request.

    Returns
    -------
    SettingInDB
        The deleted setting.

    Raises
    ------
    ObjectNotFoundError
        If the setting object with the specified `id` doesn't exist.

    """
    current = uow.config.setting.get(id)
    with uow:
        return uow.config.setting.delete(current)
