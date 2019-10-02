# -*- coding: utf-8 -*-
"""
Security-related utilities for backend API.
"""
from datetime import datetime
from datetime import timedelta
import typing as tp

import jwt
from jwt.exceptions import InvalidTokenError

from app.core import config
from app.core.jwt import ALGORITHM


PASSWORD_RESET_SUBJECT = "preset"


def generate_password_reset_token(email: str) -> str:
    """Generates a password reset token.

    Parameters
    ----------
    email : str
        The email address to generate the token for.

    Returns
    -------
    str
        The newly generated token to use.

    """
    expires_delta = timedelta(hours=config.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + expires_delta
    exp = expires.timestamp()
    return jwt.encode(
        {
            "exp": exp,
            "nbf": now,
            "sub": PASSWORD_RESET_SUBJECT,
            "email": email
        },
        config.SECRET_KEY,
        algorithm=ALGORITHM
    )


def verify_password_reset_token(token: str) -> tp.Optional[str]:
    """Verifies the given password reset token.

    Parameters
    ----------
    token : str
        The password reset token to verify.

    Returns
    -------
    str
        The user's email of the verified token (if verfied, ``None``
        otherwise).

    """
    try:
        decoded_token = jwt.decode(token, config.SECRET_KEY,
                                   algorithms=[ALGORITHM])
    except InvalidTokenError:
        return None
    if decoded_token["sub"] != PASSWORD_RESET_SUBJECT:
        return None
    return decoded_token["email"]
