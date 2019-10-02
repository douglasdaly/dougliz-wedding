# -*- coding: utf-8 -*-
"""
CRUD methods for User model objects.
"""
import typing as tp

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.core.security import get_password_hash
from app.core.security import verify_password
from app.crud.base import default_multi
from app.crud.base import persist
from app.db.models.user import User
from app.models.user import UserCreate
from app.models.user import UserUpdate


def get(db_session: Session, *, user_id: int) -> tp.Optional[User]:
    """Gets the user with the specified `user_id`.

    Parameters
    ----------
    db_session : Session
        The database session to use.
    user_id : int
        The user ID to get the User object for.

    Returns
    -------
    User
        The user with the `user_id` given (if found, ``None``
        otherwise).

    """
    return db_session.query(User).filter(User.id == user_id).first()


def get_by_email(db_session: Session, *, email: str) -> tp.Optional[User]:
    """Gets the user with the associated `email` given.

    Parameters
    ----------
    db_session : Session
        The database session to use.
    email : str
        The user's email to get the associated User object for.

    Returns
    -------
    User
        The user with the matching `email` (if found, ``None``
        otherwise).

    """
    return db_session.query(User).filter(User.email == email).first()


@default_multi
def get_multi(
    db_session: Session,
    *,
    skip: tp.Optional[int] = None,
    limit: tp.Optional[int] = None
) -> tp.List[User]:
    """Gets multiple User objects.

    Parameters
    ----------
    db_session : Session
        The database session to use.
    skip : int, optional
        The number of users to skip in this pull (default is ``0``).
    limit : int, optional
        The number of users to limit the returned values to (default is
        ``100``).

    Returns
    -------
    List[User]
        The list of User objects requested.

    """
    return db_session.query(User).offset(skip).limit(limit).all()


@persist
def create(db_session: Session, *, new_user: UserCreate) -> User:
    """Creates and stores a new User object.

    Parameters
    ----------
    db_session : Session
        The database session to use.
    new_user : UserCreate
        The new user object to create.

    Returns
    -------
    User
        The newly created User model object.

    """
    return User(
        email=new_user.email,
        name=new_user.name,
        hashed_password=get_password_hash(new_user.password),
        is_superuser=new_user.is_superuser
    )


@persist
def update(
    db_session: Session,
    *,
    user: User,
    updated_user: UserUpdate
) -> User:
    """Updates and persists changes to a User object.

    Parameters
    ----------
    db_session : Session
        The database session to use.
    user : User
        The current user object to update with the data from the given
        `updated_user`.
    updated_user : UserUpdate
        The updated user data to use for updating `user`.

    Returns
    -------
    User
        The updated User object.

    """
    user_data = jsonable_encoder(user)
    updated_data = updated_user.dict(skip_defaults=True)
    for field in user_data:
        if field in updated_data:
            setattr(user, field, updated_data[field])
    if updated_user.password:
        hashed_password = get_password_hash(updated_user.password)
        user.hashed_password = hashed_password
    return user


def authenticate(
    db_session: Session,
    *,
    email: str,
    password: str
) -> tp.Optional[User]:
    """Authenticates (and returns) the user with given credentials.

    Parameters
    ----------
    db_session : Session
        The database session to use.
    email : str
        The user's email address.
    password : str
        The plaintext password to validate.

    Returns
    -------
    User
        The authenticated User object (if verified, ``None`` otherwise).

    """
    user = get_by_email(db_session, email=email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def is_active(user: User) -> bool:
    """Verifies whether or not the given `user` is active.

    Parameters
    ----------
    user : User
        The user object to verify for being active.

    Returns
    -------
    bool
        Whether or not the given `user` is active.

    """
    return user.is_active


def is_superuser(user: User) -> bool:
    """Verifies whether or not the given `user` is a superuser.

    Parameters
    ----------
    user : User
        The user object to verify for being a superuser.

    Returns
    -------
    bool
        Whether or not the given `user` is a superuser.

    """
    return user.is_superuser
