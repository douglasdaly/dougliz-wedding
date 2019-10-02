# -*- coding: utf-8 -*-
"""
Utilities for the backend API.
"""
import re


def camel_to_snake(value: str) -> str:
    """Converts the given Camel-case name to Snake-case.

    Notes
    -----
    Originally from:
        https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case

    Parameters
    ----------
    value : str
        The value to convert to Snake-case.

    Returns
    -------
    str
        The converted `value` given.

    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', value)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
