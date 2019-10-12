# -*- coding: utf-8 -*-
"""
Utilities for the backend API.
"""
import re


def camel_to_snake(value: str) -> str:
    """Converts the given CamelCase name to snake_case.

    Notes
    -----
    Originally from:
        https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case

    Parameters
    ----------
    value : str
        The value to convert to snake_case.

    Returns
    -------
    str
        The converted `value` given.

    """
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', value)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def snake_to_camel(value: str) -> str:
    """Converts the given snake_case name to CamelCase.

    Parameters
    ----------
    value : str
        The value to convert to CamelCase.

    Returns
    -------
    str
        The converted `value` given.

    """
    s1 = re.sub(
        r'(\_)([a-z0-9])([a-z0-9]+)',
        lambda m: m.group(2).upper() + m.group(3),
        value
    )
    return re.sub(r'([0-9]*)([a-z])', lambda m: m.group(2).upper(), s1,
                  count=1)
