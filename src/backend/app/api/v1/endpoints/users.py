# -*- coding: utf-8 -*-
import typing as tp

from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.types import EmailStr
from sqlalchemy.orm import Session

from app import crud
from app.api.utils.db import get_db
from app.api.utils.security import get_current_active_superuser
from app.api.utils.security import get_current_active_user
from app.core import config
from app.db.models.user import User as DBUser
from app.models.user import User
from app.models.user import UserCreate
from app.models.user import UserInDB
from app.models.user import UserUpdate
from app.utils.email import send_new_account_email


router = APIRouter()


@router.get("/", response_model=tp.List[User])
def get_users(
    db: Session = Depends(get_db),
    skip: tp.Optional[int] = None,
    limit: tp.Optional[int] = None,
    current_user: DBUser = Depends(get_current_active_superuser)
) -> tp.List[User]:
    """Gets all the users specified.

    Parameters
    ----------
    db : Session
        The database session to use.
    skip : int, optional
        The number of users to skip in the results.
    limit : int, optional
        The number of users to return in the results.
    current_user : DBUser
        The current user making the request.

    Returns
    -------
    List[User]
        The User object(s) requested.

    """
    return crud.user.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=User)
def create_user(
    *,
    db: Session = Depends(get_db),
    new_user: UserCreate,
    current_user: DBUser = Depends(get_current_active_superuser)
) -> User:
    """Creates a new User object.

    Parameters
    ----------
    db : Session
        The database session to use.
    new_user : UserCreate
        The new user data to create a new User object with.
    current_user : DBUser
        The current user making the call.

    Returns
    -------
    User
        The newly created User object.

    Raises
    ------
    HTTPException
        If the user already exists a ``400`` error is thrown.

    """
    user = crud.user.get_by_email(db, email=new_user.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with the given username already exists"
        )
    user = crud.user.create(db, new_user=new_user)
    if config.EMAILS_ENABLED and new_user.email:
        send_new_account_email(
            email_to=new_user.email,
            username=new_user.email,
            password=new_user.password
        )
    return user


@router.put("/me", response_model=User)
def update_user_me(
    *,
    db: Session = Depends(get_db),
    password: str = Body(None),
    full_name: str = Body(None),
    email: EmailStr = Body(None),
    current_user: DBUser = Depends(get_current_active_user)
) -> User:
    """Updates the current user's profile.

    Parameters
    ----------
    db : Session
        The database session to use.
    password : str
        The new password to use.
    full_name : str
        The new full name of the user.
    email : str
        The new email to use.
    current_user: User
        The current user to update.

    Returns
    -------
    User
        The updated user.

    """
    current_user_data = jsonable_encoder(current_user)
    user_in = UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if full_name is not None:
        user_in.full_name = full_name
    if email is not None:
        user_in.email = email
    user = crud.user.update(db, user=current_user, updated_user=user_in)
    return user


@router.get("/me", response_model=User)
def read_user_me(
    db: Session = Depends(get_db),
    current_user: DBUser = Depends(get_current_active_user)
) -> User:
    """Gets the current user object.

    Parameters
    ----------
    db : Session
        The database session to use.
    current_user : User
        The current user.

    Returns
    -------
    User
        The user object.

    """
    return current_user


@router.post("/open", response_model=User)
def create_user_open(
    *,
    db: Session = Depends(get_db),
    password: str = Body(...),
    email: EmailStr = Body(...),
    full_name: str = Body(None)
) -> User:
    """Creates a new user without being logged in.

    Parameters
    ----------
    db : Session
        The database session to use.
    password : str
        The new user's password.
    email : str
        The new user's email.
    full_name : str, optional
        The full name of the new user.

    Returns
    -------
    User
        The newly created user object.

    Raises
    ------
    HTTPException
        If open registration is forbidden or a user already exists with
        the given username a ``400`` error is thrown.

    """
    if not config.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=400,
            detail="Open user registration is forbidden."
        )
    user = crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="A user with this username already exists."
        )
    new_user = UserCreate(password=password, email=email, full_name=full_name)
    user = crud.user.create(db, new_user=new_user)
    return user


@router.get("/{user_id}", response_model=User)
def read_user_by_id(
    user_id: int,
    current_user: DBUser = Depends(get_current_active_user),
    db: Session = Depends(get_db)
) -> User:
    """Gets a user from the given ID.

    Parameters
    ----------
    user_id : int
        The user ID to get the user object for.
    current_user : User
        The current user making the request.
    db : Session
        The database session to use.

    Returns
    -------
    User
        The requested user.

    Raises
    ------
    HTTPException
        If the user doesn't have the privileges to get other users then
        a ``400`` error is thrown.

    """
    user = crud.user.get(db, user_id=user_id)
    if user == current_user:
        return user
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400,
            detail="The user doesn't have sufficient privileges."
        )
    return user


@router.put("/{user_id}", response_model=User)
def update_user(
    *,
    db: Session = Depends(get_db),
    user_id: int,
    updated_user: UserUpdate,
    current_user: UserInDB = Depends(get_current_active_superuser)
) -> User:
    """Updates the given user object.

    Parameters
    ----------
    db : Session
        The database session to use.
    user_id : int
        The user ID to update.
    updated_user : UserUpdate
        The updated user data object.
    current_user : UserInDB
        The current user doing the update.

    Returns
    -------
    User
        The updated user object.

    Raises
    ------
    HTTPException
        If the user for the given `user_id` doesn't exist then a ``404``
        error is thrown.

    """
    user = crud.user.get(db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this ID doesn't exist."
        )
    user = crud.user.update(db, user=user, updated_user=updated_user)
    return user
