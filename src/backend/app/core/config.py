# -*- coding: utf-8 -*-
"""
Configuration settings for backend application.
"""
import json
import os
import typing as tp

from dotenv import load_dotenv


load_dotenv()


def getenv_bool(name: str, default: bool = False) -> bool:
    """Gets a boolean-valued environment variable.

    Parameters
    ----------
    name : str
        The environment variable to get (if it exists).
    default : bool, optional
        The default value to use (if the `name` variable doesn't exist),
        the default value is ``False``.

    Returns
    -------
    bool
        The environment variable `name` value to use.

    """
    rv = default
    env_value = os.getenv(name)
    if env_value is not None:
        rv = env_value.upper() in ('TRUE', '1')
    return rv


def getenv_int(name: str, default: tp.Optional[int] = None) -> int:
    """Gets an integer-valued environment variable.

    Parameters
    ----------
    name : str
        The environment variable to get (if it exists).
    default : int, optional
        The default value to use (if the `name` variable doesn't exist),
        the default value is ``None``.

    Returns
    -------
    int
        The environment variable `name` value to use.

    """
    rv = default
    env_value = os.getenv(name)
    if env_value is not None:
        rv = int(env_value)
    return rv


def getenv_dict(
    name: str,
    default: tp.Optional[tp.Dict[str, str]] = None
) -> tp.Dict[str, str]:
    """Gets a dictionary of values from an environment variable.

    Parameters
    ----------
    name : str
        The environment variable to get (if it exists).  Expects a
        JSON-formatted string representing a dictionary.
    default : Dict[str, str], optional
        The default value to use (if the `name` variable doesn't exist,
        the default value is ``{}``).

    Returns
    -------
    Dict[str, str]
        The dictionary from the environment variable `name`'s data.

    """
    rv = default or {}
    env_value = os.getenv(name)
    if env_value is not None:
        env_value = env_value.strip("'\" ")
        rv = json.loads(env_value)
    return rv


def getenv_list(
    name: str,
    default: tp.Optional[tp.List[str]] = None,
    *,
    seperator: str = ','
) -> tp.List[str]:
    """Gets a list of values from an environment variable.

    Parameters
    ----------
    name : str
        The environment variable to get (if it exists).  Expects a
        character-seperated string (using `seperator`).
    default : Sequence[str], optional
        The default value to use (if the `name` environment variable
        doesn't exist, the default is ``[]``).
    seperator : str, optional
        The character-seperating string to use (default is a comma).

    Returns
    -------
    Sequence[str]
        The sequence from the environment variable `name`'s data.

    """
    rv = default or []
    env_value = os.getenv(name)
    if env_value is not None:
        env_value = env_value.strip("\"' ")
        rv = [x.strip() for x in env_value.split(seperator)]
    return rv


def getenv_quotestr(
    name: str,
    default: tp.Optional[str] = None
) -> tp.Optional[str]:
    """Gets a clean environment variable as a (non-quoted) string value.

    Parameters
    ----------
    name : str
        The environment variable to get (if it exists).
    default : Sequence[str], optional
        The default value to use (if the `name` environment variable
        doesn't exist, the default is ``None``).

    Returns
    -------
    Optional[str]
        The cleaned string version of the environment variable (if it
        exists).

    """
    rv = default
    env_value = os.getenv(name)
    if env_value is not None:
        if env_value[0] == env_value[-1] and env_value[0] in ('"', "'"):
            rv = env_value[1:-1]
        else:
            rv = env_value
    return rv


# Environment
DEBUG = getenv_bool('DEBUG')

# General
API_VERSION = os.getenv('API_VERSION')
PROJECT_NAME = getenv_quotestr('PROJECT_NAME')
SERVER_NAME = os.getenv('SERVER_NAME')
SERVER_HOST = os.getenv('SERVER_HOST')
SERVER_PORT = getenv_int('SERVER_PORT')

# Security
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8  # 8 days
ALLOWED_ORIGINS = getenv_list('ALLOWED_ORIGINS')
EMAIL_RESET_TOKEN_EXPIRE_HOURS = 24

SECRET_KEY = os.getenv('SECRET_KEY')
if SECRET_KEY is None:
    if not DEBUG:
        raise EnvironmentError("Must provide SECRET_KEY in production")
    SECRET_KEY = os.urandom(32)
else:
    SECRET_KEY = SECRET_KEY.encode()

# Storages
STORAGE_TYPE = os.getenv('STORAGE_TYPE', 'database')

# - Database
DB_ENGINE = os.getenv('DB_ENGINE')
DB_DRIVER = os.getenv('DB_DRIVER')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = getenv_int('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_CONNECT_EXTRA = getenv_dict('DB_CONNECT_EXTRA')

# Emails
EMAILS_ENABLED = getenv_bool("EMAILS_ENABLED")

EMAILS_FROM_EMAIL = os.getenv("EMAILS_FROM_EMAIL")
EMAILS_FROM_NAME = os.getenv("EMAILS_FROM_NAME")
EMAILS_TEMPLATE_DIR = os.getenv("EMAILS_TEMPLATE_DIR")

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_PORT = getenv_int("SMTP_PORT")
SMTP_TLS = getenv_bool("SMTP_TLS")
SMTP_USER = os.getenv("SMTP_USER")

# Users
USERS_OPEN_REGISTRATION = getenv_bool("USERS_OPEN_REGISTRATION", False)

# - Initial Superuser
SUPERUSER_EMAIL = getenv_quotestr('SUPERUSER_EMAIL')
SUPERUSER_PASSWORD = getenv_quotestr('SUPERUSER_PASSWORD')
