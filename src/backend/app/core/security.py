# -*- coding: utf-8 -*-
"""
Core security functionality for the backend API.
"""
import typing as tp

from passlib.context import CryptContext
from pydantic import SecretStr


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(
    plain_password: tp.Union[str, SecretStr],
    hashed_password: str
) -> bool:
    """Verifies the given plaintext password against the hash.

    Parameters
    ----------
    plain_password : str
        The plaintext password to verify.
    hashed_password : str
        The password hash to verify the given `plain_password` against.

    Returns
    -------
    bool
        Whether or not the given password matches the given hash.

    """
    if isinstance(plain_password, SecretStr):
        plain_password = plain_password.get_secret_value()
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: tp.Union[str, SecretStr]) -> str:
    """Gets the hashed password from the given plaintext.

    Parameters
    ----------
    password : str
        The plaintext password to compute the hash for.

    Returns
    -------
    str
        The hashed password.

    """
    if isinstance(password, SecretStr):
        password = password.get_secret_value()
    return pwd_context.hash(password)
