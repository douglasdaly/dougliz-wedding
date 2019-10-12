# -*- coding: utf-8 -*-
"""
Core utilities for API.
"""
import importlib

from fastapi import APIRouter

from app.core import config


def load_api_router(version: str) -> APIRouter:
    """Loads the API router for the version specified.

    Parameters
    ----------
    version : str
        The version of the API to load the router for (e.g. ``'v1'``).

    Returns
    -------
    APIRouter
        The API router requested.

    Raises
    ------
    ValueError
        If the specified `version` of the API specification is could not
        be found.

    """
    try:
        rv = importlib.import_module(f"app.api.{version}.api")
        return rv.api_router
    except ImportError:
        if config.DEBUG:
            raise
        raise ValueError(f"Version not found: {version}")
