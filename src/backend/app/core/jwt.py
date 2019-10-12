# -*- coding: utf-8 -*-
"""
JSON Web Token functionality.
"""
from datetime import datetime
from datetime import timedelta
import typing as tp

import jwt

from app.core import config
from app.utils.jsonutils import JSONEncoderUUID


ACCESS_TOKEN_SUBJECT = "access"
ALGORITHM = "HS256"
DEFAULT_EXPIRES_DELTA = timedelta(minutes=15)


def create_access_token(
    data: tp.Mapping[str, tp.Any],
    *,
    expires_delta: tp.Optional[timedelta] = None
) -> str:
    """Creates a new JWT access token to use.

    Parameters
    ----------
    data : Mapping[str, Any]
        The data to create an access token with.
    expires_delta : timedelta, optional
        The time to expiration of the generated token.

    Returns
    -------
    str
        The JSON Web Token string to use.

    """
    to_encode = data.copy()
    expires_delta = expires_delta or DEFAULT_EXPIRES_DELTA
    expires = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expires, "sub": ACCESS_TOKEN_SUBJECT})
    return jwt.encode(
        to_encode,
        config.SECRET_KEY,
        algorithm=ALGORITHM,
        json_encoder=JSONEncoderUUID
    )
