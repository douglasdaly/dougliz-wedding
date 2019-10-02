# -*- coding: utf-8 -*-
from datetime import timedelta
import typing as tp

from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud
from app.api.utils.db import get_db
from app.api.utils.security import get_current_user
from app.core import config
from app.core.jwt import create_access_token
from app.core.security import get_password_hash
from app.db.models.user import User as DBUser
from app.models.message import Message
from app.models.token import Token
from app.models.user import User
from app.utils.security import generate_password_reset_token
from app.utils.security import verify_password_reset_token
from app.utils.email import send_password_reset_email


router = APIRouter()


@router.post("/login/access-token", response_model=Token, tags=["login"])
def login_access_token(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> tp.Mapping[str, str]:
    """OAuth2 compatible token login.

    Acquires an access token to be used for future requests.

    Parameters
    ----------
    db : Session
        The database session to use.
    form_data : OAuth2PasswordRequestForm
        The OAuth2 request form data to use.

    Returns
    -------
    Mapping[str, str]
        A mapping of access token data.

    Raises
    ------
    HTTPException
        If the user could not be logged or is not an active user then a
        ``400`` error is raised.

    """
    user = crud.user.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=400, detail="Invalid username or password"
        )
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(
        minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return {
        "access_token": create_access_token(
            {"user_id": user.id}, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/login/test-token", tags=["login"], response_model=User)
def test_token(current_user: DBUser = Depends(get_current_user)) -> DBUser:
    """Tests the given authentication token for validity.

    Parameters
    ----------
    current_user : User
        The current user to test the token for.

    Returns
    -------
    User
        The user with the valid token.

    """
    return current_user


@router.post('/password-recovery/{email}', tags=["login"],
             response_model=Message)
def recover_password(
    email: str,
    db: Session = Depends(get_db)
) -> tp.Mapping[str, str]:
    """Send a password recovery email to the user.

    Parameters
    ----------
    email : str
        The email address to send a password recovery email for.
    db : Session
        The database session object to use.

    Returns
    -------
    Mapping[str, str]
        The message from the password recovery result.

    Raises
    ------
    HTTPException
        If no username is found for the given `email` then a ``404``
        error is thrown.

    """
    user = crud.user.get_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=404, detail="No user exists for the given email"
        )
    password_reset_token = generate_password_reset_token(email=email)
    send_password_reset_email(
        email_to=user.email, email=email, token=password_reset_token
    )
    return {"value": "Password recovery email sent."}


@router.post("/reset-password/", tags=["login"], response_model=Message)
def reset_password(
    token: str = Body(...),
    new_password: str = Body(...),
    db: Session = Depends(get_db)
) -> tp.Mapping[str, str]:
    """Resets a user's password from the given reset token.

    Parameters
    ----------
    token : str
        The password reset token to use.
    new_password : str
        The new, plaintext password to set.
    db : Session
        The database session object to use.

    Returns
    -------
    Mapping[str, str]
        The message from the password reset result.

    Raises
    ------
    HTTPException
        If the token isn't valid, the user associated with the token
        doesn't exist, or is not an active user then a ``400`` error is
        thrown.

    """
    email = verify_password_reset_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = crud.user.get_by_email(db, email=email)
    if not user:
        raise HTTPException(status_code=400, detail="The user doesn't exist")
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    hashed_password = get_password_hash(new_password)
    user.hashed_password = hashed_password
    db.add(user)
    db.commit()
    return {"value": "Password updated successfully"}
