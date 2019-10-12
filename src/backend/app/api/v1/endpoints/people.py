# -*- coding: utf-8 -*-
"""
People API endpoints.
"""
import typing as tp
from uuid import UUID

from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import Query

from app import exceptions
from app.api.utils.security import get_current_active_user
from app.api.utils.security import get_current_active_poweruser
from app.api.utils.storage import get_uow
from app.crud.core import UnitOfWork
from app.db.models.person import Person as DBPerson
from app.models.person import Person
from app.models.person import PersonCreate
from app.models.person import PersonUpdate
from app.models.user import UserInDB


router = APIRouter()


@router.post("/", response_model=Person)
async def create_person(
    *,
    new_person: PersonCreate = Body(...),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> DBPerson:
    """Creates a new Person object.

    Parameters
    ----------
    new_person : PersonCreate
        The new person data to create a new Person object with.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current poweruser making the call.

    Returns
    -------
    DBPerson
        The newly created Person object.

    Raises
    ------
    ObjectExistsException
        If a person associated with the given name already exists.

    """
    if isinstance(new_person.name, UUID):
        if uow.person.get_by_name_id(new_person.name):
            raise exceptions.ObjectExistsException(Person, 'name')

    with uow:
        return uow.person.create(new_person)


@router.get("/", response_model=tp.List[Person])
async def read_people(
    *,
    skip: tp.Optional[int] = Query(None),
    limit: tp.Optional[int] = Query(None),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> tp.List[DBPerson]:
    """Gets all the people specified.

    Parameters
    ----------
    skip : int, optional
        The number of people to skip in the results.
    limit : int, optional
        The number of people to return in the results.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current power user making the request.

    Returns
    -------
    List[DBPerson]
        The Person object(s) requested.

    """
    return uow.person.all(skip=skip, limit=limit)


@router.get('/id/{person_id}', response_model=Person)
async def read_person(
    person_id: UUID,
    *,
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_user)
) -> DBPerson:
    """Gets a single user with the specified `id`.

    Parameters
    ----------
    person_id : UUID
        The UUID of the person to get.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current power user making the request.

    Returns
    -------
    DBPerson
        The requested person.

    Raises
    ------
    ObjectNotFoundException
        If the requested person is not found.
    PrivilegeException
        If the current user doesn't have sufficient privileges to view
        other people.

    """
    person = uow.person.get(person_id)
    if not current_user.is_poweruser and current_user.person != person:
        raise exceptions.PrivilegeException()
    if not person:
        raise exceptions.ObjectNotFoundException(Person, 'id')
    return person


@router.get("/me", response_model=Person)
def read_person_me(
    *,
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_user)
) -> tp.Optional[DBPerson]:
    """Gets the person object associated with the current user."""
    return current_user.person


@router.put('/id/{person_id}', response_model=Person)
async def update_person(
    person_id: UUID,
    *,
    updated_person: PersonUpdate = Body(...),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_user)
) -> DBPerson:
    """Updates the specified person object.

    Parameters
    ----------
    person_id : UUID
        The ID of the person object to update.
    updated_person : PersonUpdate
        The update data to use.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current user making the request.

    Returns
    -------
    DBPerson
        The updated person object.

    Raises
    ------
    ObjectNotFoundException
        If the person with the specified `id` doesn't exist.
    PrivilegeException
        If the user making the request doesn't have sufficient
        permissions.

    """
    person = uow.person.get(person_id)
    if not current_user.is_poweruser or person != current_user.person:
        raise exceptions.PrivilegeException()
    if not person:
        raise exceptions.ObjectNotFoundException(Person, 'id')
    with uow:
        return uow.person.update(person, updated_person)


@router.put("/me", response_model=Person)
async def update_person_me(
    *,
    updated_person: PersonUpdate = Body(...),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_user)
) -> DBPerson:
    """Updates the specified person object.

    Parameters
    ----------
    updated_person : PersonUpdate
        The update data to use.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current user making the request.

    Returns
    -------
    DBPerson
        The updated person object.

    Raises
    ------
    ObjectNotFoundException
        If the person object for the current user doesn't exist.

    """
    if not current_user.person:
        raise exceptions.ObjectNotFoundException(Person)
    with uow:
        return uow.person.update(current_user.person, updated_person)


@router.delete("/id/{person_id}", response_model=Person)
async def delete_person(
    person_id: UUID,
    *,
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> DBPerson:
    """Deletes the specified person."""
    person = uow.person.get(person_id, raise_ex=True)
    with uow:
        return uow.person.delete(person)
