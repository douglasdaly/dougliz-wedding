# -*- coding: utf-8 -*-
"""
Address API endpoints.
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
from app.db.models.address import Address as DBAddress
from app.models.user import UserInDB
from app.models.address import Address
from app.models.address import AddressCreate
from app.models.address import AddressUpdate


router = APIRouter()


@router.post("/", response_model=Address)
async def create_address(
    *,
    new_address: AddressCreate = Body(...),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> DBAddress:
    """Creates a new Address object.

    Parameters
    ----------
    new_address : AddressCreate
        The new address data to create a new Address object with.
    uow : UnitOfWork
        The unit of work object to use.
    current_user : UserInDB
        The current user making the call.

    Returns
    -------
    Address
        The newly created Address object.

    """
    with uow:
        return uow.address.create(new_address)


@router.get("/{address_id}", response_model=Address)
async def read_address(
    address_id: UUID,
    *,
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> DBAddress:
    """Gets the Address from the given ID.

    Parameters
    ----------
    address_id : int
        The address ID to get the Address object for.
    uow : UnitOfWork
        The unit of work object to use.
    current_user : UserInDB
        The current user making the request.

    Returns
    -------
    Address
        The requested Address.

    """
    return uow.address.get(address_id)


@router.get("/", response_model=tp.List[Address])
async def read_addresses(
    *,
    skip: tp.Optional[int] = Query(None),
    limit: tp.Optional[int] = Query(None),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> tp.List[DBAddress]:
    """Gets all the addresses specified.

    Parameters
    ----------
    skip : int, optional
        The number of addresses to skip in the results.
    limit : int, optional
        The number of addresses to return in the results.
    uow : UnitOfWork
        The unit of work object to use.
    current_user : UserInDB
        The current user making the request.

    Returns
    -------
    List[Address]
        The Address object(s) requested.

    """
    return uow.address.all(skip=skip, limit=limit)


@router.put("/{address_id}", response_model=Address)
async def update_address(
    address_id: UUID,
    *,
    updated_address: AddressUpdate = Body(...),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> DBAddress:
    """Updates the given Address object.

    Parameters
    ----------
    address_id : int
        The address ID to get the Address object for.
    updated_address: AddressUpdate
        The updated address data object.
    uow : UnitOfWork
        The unit of work object to use.
    current_user : UserInDB
        The current user making the request.

    Returns
    -------
    Address
        The requested Address.

    Raises
    ------
    ObjectNotFoundException
        If the address for the given `address_id` doesn't exist.

    """
    address = uow.address.get(address_id, raise_ex=True)
    with uow:
        return uow.address.update(address, updated_address)


@router.delete("/{address_id}", response_model=Address)
async def delete_address(
    address_id: UUID,
    *,
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> DBAddress:
    """Updates the given Address object.

    Parameters
    ----------
    address_id : int
        The address ID of the address to delete.
    uow : UnitOfWork
        The unit of work object to use.
    current_user : UserInDB
        The current user making the request.

    Returns
    -------
    Address
        The deleted Address.

    Raises
    ------
    ObjectNotFoundException
        If the address for the given `address_id` doesn't exist.

    """
    address = uow.address.get(address_id, raise_ex=True)
    with uow:
        return uow.address.delete(address)
