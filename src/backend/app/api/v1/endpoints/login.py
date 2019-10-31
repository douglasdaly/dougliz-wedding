# -*- coding: utf-8 -*-
"""
Login API endpoints.
"""
from datetime import timedelta
import typing as tp

from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.api.utils.storage import get_uow
from app.api.utils.security import get_current_user
from app.core import config
from app.core.jwt import create_access_token
from app.crud.core import UnitOfWork
from app.db.models.user import User as DBUser
from app.exceptions import APIError
from app.models.message import Message
from app.models.token import Token
from app.models.user import User
from app.models.user import UserUpdate
from app.models.user import UserInDB
from app.utils.security import generate_password_reset_token
from app.utils.security import verify_password_reset_token
from app.utils.email import send_password_reset_email


router = APIRouter()


@router.post("/login/access-token", response_model=Token)
async def login_access_token(
    *,
    form_data: OAuth2PasswordRequestForm = Depends(),
    uow: UnitOfWork = Depends(get_uow)
) -> tp.Mapping[str, str]:
    """OAuth2 compatible token login.

    Acquires an access token to be used for future requests.

    Parameters
    ----------
    form_data : OAuth2PasswordRequestForm
        The OAuth2 request form data to use.
    uow : UnitOfWork
        The unit of work object to use.

    Returns
    -------
    Mapping[str, str]
        A mapping of access token data.

    Raises
    ------
    APIException
        If the user could not be logged or is not an active user.

    """
    user = uow.user.authenticate(form_data.username, form_data.password)
    if not user:
        raise APIError("Invalid username or password")
    elif not user.is_active:
        raise APIError("Inactive user")
    access_token_expires = timedelta(
        minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = create_access_token(
        {"user_id": user.uid},
        expires_delta=access_token_expires
    )
    return {'accessToken': access_token, 'tokenType': "bearer"}


@router.post("/login/test-token", response_model=User)
async def test_token(
    *,
    current_user: UserInDB = Depends(get_current_user)
) -> DBUser:
    """Tests the given authentication token for validity.

    Parameters
    ----------
    current_user : UserInDB
        The current user to test the token for.

    Returns
    -------
    User
        The user with the valid token.

    """
    return current_user


@router.post('/password-recovery/{email}', response_model=Message)
async def recover_password(
    email: str,
    *,
    uow: UnitOfWork = Depends(get_uow)
) -> tp.Mapping[str, str]:
    """Send a password recovery email to the user.

    Parameters
    ----------
    email : str
        The email address to send a password recovery email for.
    uow : UnitOfWork
        The unit of work object to use.

    Returns
    -------
    Mapping[str, str]
        The message from the password recovery result.

    """
    user = uow.user.get_by_email(email)
    if user:
        password_reset_token = generate_password_reset_token(email=email)
        send_password_reset_email(
            email_to=user.email, email=email, token=password_reset_token
        )
    return {"value": "Password recovery email sent."}


@router.post("/reset-password/", response_model=Message)
async def reset_password(
    *,
    token: str = Body(...),
    new_password: str = Body(...),
    uow: UnitOfWork = Depends(get_uow)
) -> tp.Mapping[str, str]:
    """Resets a user's password from the given reset token.

    Parameters
    ----------
    token : str
        The password reset token to use.
    new_password : str
        The new, plaintext password to set.
    uow : UnitOfWork
        The unit of work object to use.

    Returns
    -------
    Mapping[str, str]
        The message from the password reset result.

    Raises
    ------
    APIException
        If the token isn't valid, or the user associated is not an
        active user.
    ObjectNotFoundException
        If the user specified by the decoded token does not exist.

    """
    email = verify_password_reset_token(token)
    if not email:
        raise APIError("Invalid token.")

    user = uow.user.get_by_email(email, raise_ex=True)
    if not uow.user.is_active(user):
        raise APIError("Inactive user.")

    updated_user = UserUpdate(password=new_password)
    with uow:
        uow.user.update(user, updated_user)
    return {"value": "Password updated successfully"}
