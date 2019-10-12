# -*- coding: utf-8 -*-
"""
Security-related utilities for the API.
"""
from uuid import UUID

from fastapi import Depends
from fastapi import Security
from fastapi.security import OAuth2PasswordBearer
import jwt

from app import exceptions
from app.api.utils.storage import get_uow
from app.core import config
from app.core.jwt import ALGORITHM
from app.crud.core import UnitOfWork
from app.db.models.user import User
from app.models.token import TokenPayload


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"/api/login/access-token"
)


def get_current_user(
    uow: UnitOfWork = Depends(get_uow),
    token: str = Security(reusable_oauth2)
) -> User:
    """Gets the current User object from the given token.

    Parameters
    ----------
    uow : UnitOfWork
        The unit of work to use.
    token : str
        The token to get the user from.

    Returns
    -------
    User
        The User model object for the current user.

    Raises
    ------
    HTTPException
        If the token could not be validated a ``403`` error is raised.
        If the user from the valid token could not be found then a
        ``404`` error is raised.

    """
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[ALGORITHM])
        payload['user_id'] = UUID(payload['user_id'])
    except jwt.PyJWTError:
        raise exceptions.PrivilegeError(
            "Could not validate the given credentials."
        )
    token_data = TokenPayload(**payload)
    return uow.user.get(token_data.user_id, raise_ex=True)


def get_current_active_user(
    current_user: User = Security(get_current_user)
) -> User:
    """Gets whether or not the current user is an active user.

    Parameters
    ----------
    current_user : User
        The user to check for active status.

    Returns
    -------
    User
        The current, active user object.

    Raises
    ------
    HTTPException
        If the given `current_user` is not an active user then a ``400``
        error is raised.

    """
    if not current_user.is_active:
        raise exceptions.APIError("Inactive user")
    return current_user


def get_current_active_poweruser(
    current_user: User = Security(get_current_active_user)
) -> User:
    """Gets whether or not the given user is a power user.

    Parameters
    ----------
    current_user : User
        The current user to check for poweruser status.

    Returns
    -------
    User
        The current, active poweruser object.

    Raises
    ------
    HTTPException
        If the current user is not a poweruser then a ``400`` error is
        raised.

    """
    if not current_user.is_poweruser:
        raise exceptions.PrivilegeError()
    return current_user


def get_current_active_superuser(
    current_user: User = Security(get_current_active_user)
) -> User:
    """Gets whether or not the given user is a superuser.

    Parameters
    ----------
    current_user : User
        The current user to check for superuser status.

    Returns
    -------
    User
        The current, active superuser object.

    Raises
    ------
    HTTPException
        If the current user is not a superuser then a ``400`` error is
        raised.

    """
    if not current_user.is_superuser:
        raise exceptions.PrivilegeError()
    return current_user
