# -*- coding: utf-8 -*-
"""
Wedding API endpoints.
"""
import typing as tp

from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends

from app.api.utils.security import get_current_active_poweruser
from app.api.utils.security import get_current_active_user
from app.api.utils.storage import get_uow
from app.crud.core import UnitOfWork
from app.db.models.wedding import WeddingInfo as DBWeddingInfo
from app.models.user import UserInDB
from app.models.wedding.wedding_info import WeddingInfo
from app.models.wedding.wedding_info import WeddingInfoCreate
from app.models.wedding.wedding_info import WeddingInfoUpdate


router = APIRouter()


@router.get("/", response_model=WeddingInfo)
async def read_wedding_info(
    *,
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_user)
) -> tp.Optional[DBWeddingInfo]:
    """Gets the wedding information object.

    Parameters
    ----------
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current user making the call.

    Returns
    -------
    Optional[DBWeddingInfo]
        The wedding information requested.

    """
    return uow.wedding.wedding_info.get()


@router.post("/", response_model=WeddingInfo)
async def create_wedding_info(
    *,
    new_wedding_info: WeddingInfoCreate = Body(...),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> DBWeddingInfo:
    """Creates a new wedding information object.

    Parameters
    ----------
    new_wedding_info : WeddingInfoCreate
        The information to use to create the new wedding information
        object.
    uow : UnitOfWork
        The unit of work object to use.
    current_user : UserInDB
        The current poweruser making the request.

    Returns
    -------
    WeddingInfo
        The newly created wedding information object.

    Raises
    ------
    ObjectExistsError
        If the wedding information object already exists.

    """
    with uow:
        return uow.wedding.wedding_info.create(new_wedding_info)


@router.put("/", response_model=WeddingInfo)
async def update_wedding_info(
    *,
    updated_wedding_info: WeddingInfoUpdate = Body(...),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> DBWeddingInfo:
    """Updates the wedding information object.

    Parameters
    ----------
    updated_wedding_info : WeddingInfoUpdate
        The information to use to update the wedding information object.
    uow : UnitOfWork
        The unit of work object to use.
    current_user : UserInDB
        The current poweruser making the request.

    Returns
    -------
    WeddingInfo
        The updated wedding information object.

    Raises
    ------
    ObjectNotFoundError
        If the wedding information doesn't exist.

    """
    curr_info = uow.wedding.wedding_info.get(raise_ex=True)
    with uow:
        return uow.wedding.wedding_info.update(curr_info, updated_wedding_info)
