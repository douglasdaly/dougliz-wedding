# -*- coding: utf-8 -*-
"""
Database-related utilities for the API.
"""
from starlette.requests import Request
from sqlalchemy.orm import Session

from app.crud.core import UnitOfWork


def get_db(request: Request) -> Session:
    """Gets the database session stored on the request state.

    Parameters
    ----------
    request : Request
        The API request object to fetch the database session object
        from.

    Returns
    -------
    Session
        The SQLAlchemy database session object to use.

    """
    return request.state.db


def get_uow(request: Request) -> UnitOfWork:
    """Gets the unit of work object stored on the request state.

    Parameters
    ----------
    request : Request
        The API request object to fetch the unit of work object from.

    Returns
    -------
    UnitOfWork
        The unit of work object stored on the request's state.

    """
    return request.state.uow
