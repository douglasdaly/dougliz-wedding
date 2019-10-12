# -*- coding: utf-8 -*-
"""
Property-related utilities.
"""
import functools
import typing as tp


class lazy_property(object):
    """
    Lazily-evaluated property decorator.
    """

    def __init__(self, func: tp.Callable) -> None:
        self._function = func
        functools.update_wrapper(self, func)

    def __get__(self, obj, obj_type) -> tp.Any:
        if obj is None:
            return self
        val = self._function(obj)
        obj.__dict__[self._function.__name__] = val
        return val
