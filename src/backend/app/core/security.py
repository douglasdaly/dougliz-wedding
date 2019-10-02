# -*- coding: utf-8 -*-
"""
Core security functionality for the backend API.
"""
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
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
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
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
    return pwd_context.hash(password)
