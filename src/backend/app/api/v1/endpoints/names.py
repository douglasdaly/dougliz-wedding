# -*- coding: utf-8 -*-
"""
Names API endpoints.
"""
import typing as tp
from uuid import UUID

from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import Query

from app.api.utils.security import get_current_active_poweruser
from app.api.utils.storage import get_uow
from app.crud.core import UnitOfWork
from app.models.name import Name
from app.models.name import NameCreate
from app.models.name import NameUpdate
from app.models.user import UserInDB


router = APIRouter()


@router.post("/", response_model=Name)
async def create_name(
    *,
    new_name: NameCreate = Body(...),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> Name:
    """Creates a new Name object.

    Parameters
    ----------
    new_name : NameCreate
        The new name data to create a new Name object with.
    uow : UnitOfWork
        The unit of work to use.
    current_user : User
        The currently active poweruser making the request.

    Returns
    -------
    Name
        The newly created Name object.

    """
    with uow:
        return uow.name.create(new_name)


@router.get("/{name_id}", response_model=Name)
async def read_name_by_id(
    name_id: UUID,
    *,
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> Name:
    """Gets the name with the specified ID.

    Parameters
    ----------
    name_id : UUID
        The name ID to get the name for.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The currently active poweruser making the request.

    Returns
    -------
    List[Name]
        The Name object(s) requested.

    """
    return uow.name.get(name_id)


@router.get("/", response_model=tp.List[Name])
async def read_names(
    *,
    skip: tp.Optional[int] = Query(None),
    limit: tp.Optional[int] = Query(None),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> tp.List[Name]:
    """Gets all the names specified.

    Parameters
    ----------
    skip : int, optional
        The number of names to skip in the results.
    limit : int, optional
        The number of names to return in the results.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The currently active poweruser making the request.

    Returns
    -------
    List[Name]
        The Name object(s) requested.

    """
    return uow.name.all(skip=skip, limit=limit)


@router.put("/{name_id}", response_model=Name)
async def update_name(
    name_id: UUID,
    *,
    updated_name: NameUpdate = Body(...),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> Name:
    """Updates an existing Name object.

    Parameters
    ----------
    name_id : UUID
        The name ID to update.
    updated_name : NameUpdate
        The updated name data to use.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current active poweruser making the request.

    Returns
    -------
    Name
        The updated Name object.

    """
    name = uow.name.get(name_id, raise_ex=True)
    with uow:
        return uow.name.update(name, updated_name)
