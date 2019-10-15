# -*- coding: utf-8 -*-
"""
Users API endpoints.
"""
import typing as tp
from uuid import UUID

from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import Query

from app import exceptions
from app.api.utils.security import get_current_active_superuser
from app.api.utils.security import get_current_active_user
from app.api.utils.storage import get_uow
from app.core import config
from app.crud.core import UnitOfWork
from app.db.models.user import User as DBUser
from app.models.user import User
from app.models.user import UserCreate
from app.models.user import UserInDB
from app.models.user import UserUpdate
from app.utils.email import send_new_account_email


router = APIRouter()


@router.post("/", response_model=User)
async def create_user(
    *,
    new_user: UserCreate = Body(...),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_superuser)
) -> DBUser:
    """Creates a new User object.

    Parameters
    ----------
    new_user : UserCreate
        The new user data to create a new User object with.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current user making the call.

    Returns
    -------
    User
        The newly created User object.

    Raises
    ------
    ObjectExistsException
        If the user already exists.

    """
    user = uow.user.get_by_email(new_user.email)
    if user:
        raise exceptions.ObjectExistsException(User, 'email')
    with uow:
        user = uow.user.create(new_user)
    if config.EMAILS_ENABLED and new_user.email:
        send_new_account_email(
            email_to=new_user.email,
            username=new_user.email,
            password=new_user.password
        )
    return user


@router.post("/open", response_model=User)
async def create_user_open(
    *,
    new_user: UserCreate = Body(...),
    uow: UnitOfWork = Depends(get_uow)
) -> DBUser:
    """Creates a new user without being logged in.

    Parameters
    ----------
    new_user : UserCreate
        The new user to create.
    uow : UnitOfWork
        The unit of work to use.

    Returns
    -------
    DBUser
        The newly created user object.

    Raises
    ------
    APIException
        If open registration is forbidden.
    ObjectExistsException
        If a user already exists with the given email.

    """
    if not config.USERS_OPEN_REGISTRATION:
        raise exceptions.APIException("Open user registration is forbidden.")
    user = uow.user.get_by_email(new_user.email)
    if user:
        raise exceptions.ObjectExistsException(User, 'email')
    with uow:
        return uow.user.create(new_user)


@router.get("/", response_model=tp.List[User])
async def read_users(
    *,
    skip: tp.Optional[int] = Query(None),
    limit: tp.Optional[int] = Query(None),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_superuser)
) -> tp.List[DBUser]:
    """Gets all the users specified.

    Parameters
    ----------
    skip : int, optional
        The number of users to skip in the results.
    limit : int, optional
        The number of users to return in the results.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current user making the request.

    Returns
    -------
    List[DBUser]
        The User object(s) requested.

    """
    return uow.user.all(skip=skip, limit=limit)


@router.get("/id/{user_id}", response_model=User)
async def read_user(
    user_id: UUID,
    *,
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_user)
) -> DBUser:
    """Gets a user from the given ID.

    Parameters
    ----------
    user_id : UUID
        The user ID to get the User object for.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current user making the request.

    Returns
    -------
    DBUser
        The requested user.

    Raises
    ------
    PrivilegeException
        If the user doesn't have sufficient privileges to read other
        users.
    ObjectNotFoundError
        If the user with the specified `id` doesn't exist.

    """
    user = uow.user.get(user_id)
    if user == current_user:
        return user
    if not current_user.is_superuser:
        raise exceptions.PrivilegeException()
    if user is None:
        raise exceptions.ObjectNotFoundException(User, 'id')
    return user


@router.get("/me", response_model=User)
async def read_user_me(
    *,
    current_user: UserInDB = Depends(get_current_active_user)
) -> DBUser:
    """Gets the current user object.

    Parameters
    ----------
    current_user : UserInDB
        The current user.

    Returns
    -------
    DBUser
        The user object.

    """
    return current_user


@router.put("/id/{user_id}", response_model=User)
async def update_user(
    user_id: UUID,
    *,
    updated_user: UserUpdate = Body(...),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_superuser)
) -> DBUser:
    """Updates the given user object.

    Parameters
    ----------
    user_id : UUID
        The user ID to update.
    updated_user : UserUpdate
        The updated user data object.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current user doing the update.

    Returns
    -------
    DBUser
        The updated user object.

    Raises
    ------
    ObjectNotFoundException
        If the user for the given `user_id` doesn't exist.

    """
    user = uow.user.get(user_id, raise_ex=True)
    with uow:
        return uow.user.update(user, updated_user)


@router.put("/me", response_model=User)
async def update_user_me(
    *,
    current_password: str = Body(..., alias='currentPassword'),
    updated_user: UserUpdate = Body(..., alias='updatedUser'),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_user)
) -> DBUser:
    """Updates the current user's profile.

    Parameters
    ----------
    current_password : str
        The user's current password (for verification).
    updated_user : UserUpdate
        The data to use for updating the current user.
    uow : UnitOfWork
        The unit of work to use.
    current_user: UserInDB
        The current user to update.

    Returns
    -------
    DBUser
        The updated user.

    Raises
    ------
    APIException
        If the `current_password` given is incorrect.

    """
    auth_user = uow.user.authenticate(current_user.email, current_password)
    if auth_user is None or auth_user != current_user:
        raise exceptions.APIException("Invalid credentials.")
    with uow:
        return uow.user.update(current_user, updated_user)


@router.delete("/id/{user_id}", response_model=User)
async def delete_user(
    user_id: UUID,
    *,
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_superuser)
) -> DBUser:
    """Deletes the specified User.

    Parameters
    ----------
    user_id : UUID
        The ID of the user to remove.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current active superuser making the request.

    Returns
    -------
    DBUser
        The user object removed.

    Raises
    ------
    APIException
        If the `current_user` is the user to delete.
    ObjectNotFoundException
        If no user is found for the given `id`.

    """
    user = uow.user.get(user_id, raise_ex=True)
    if user == current_user:
        raise exceptions.APIException("Cannot remove yourself.")
    with uow:
        return uow.user.delete(user)
