# -*- coding: utf-8 -*-
"""
Base functionality for the CRUD-related modules.
"""
from functools import wraps
import typing as tp

from sqlalchemy.orm import Session


def default_multi(func: tp.Callable) -> tp.Callable:
    """Decorator to set default input parameters if not set.

    Parameters
    ----------
    func : Callable
        The function to wrap and process input parameters for.

    Returns
    -------
    Callable
        The wrapped function to use.

    """
    @wraps(func)
    def _wrapper(*args, **kwargs):
        if kwargs.setdefault('skip', 0) is None:
            kwargs['skip'] = 0
        if kwargs.setdefault('limit', 100) is None:
            kwargs['limit'] = 100
        return func(*args, **kwargs)

    return _wrapper


def persist(func: tp.Callable) -> tp.Callable:
    """Decorator to persist the object returned from the given `func`.

    Parameters
    ----------
    func : Callable
        The function to wrap and persist the result object of.

    Returns
    -------
    Callable
        The wrapped function to use.

    """
    @wraps(func)
    def _wrapper(db_session: Session, *args, **kwargs):
        rv = func(db_session, *args, **kwargs)
        db_session.add(rv)
        db_session.commit()
        db_session.refresh(rv)
        return rv

    return _wrapper
