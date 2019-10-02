# -*- coding: utf-8 -*-
"""
Database-related utilities for the API.
"""
from starlette.requests import Request
from sqlalchemy.orm import Session


def get_db(request: Request) -> Session:
    """Gets the database session stored on the request.

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
