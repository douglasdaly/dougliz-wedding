# -*- coding: utf-8 -*-
"""
Security-related utilities for the API.
"""
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Security
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt import PyJWTError
from sqlalchemy.orm import Session
from starlette.status import HTTP_403_FORBIDDEN

from app import crud
from app.api.utils.db import get_db
from app.core import config
from app.core.jwt import ALGORITHM
from app.db.models.user import User
from app.models.token import TokenPayload


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"/api/login/access-token"
)


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Security(reusable_oauth2)
) -> User:
    """Gets the current User object from the given token.

    Parameters
    ----------
    db : Session
        The database session to use.
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
    except PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="Could not validate the given credentials."
        )
    token_data = TokenPayload(**payload)
    user = crud.user.get(db, user_id=token_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


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
    if not crud.user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
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
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user
