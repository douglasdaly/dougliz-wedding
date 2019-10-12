# -*- coding: utf-8 -*-
#
#   This module is part of the Frequent project, Copyright (C) 2019,
#   Douglas Daly.  The Frequent package is free software, licensed under
#   the MIT License.
#
#   Source Code:
#       https://github.com/douglasdaly/frequent-py
#   Documentation:
#       https://frequent-py.readthedocs.io/en/latest
#   License:
#       https://frequent-py.readthedocs.io/en/latest/license.html
#
"""
Singleton utility metaclass.

Simply add it to any class you want to behave like a singleton via the
`metaclass`:

.. code-block:: python
    class MyClass(SomeBaseClass, metaclass=Singleton):
        def __init__(self, x: int) -> None:
            self.x = x
            return


Examples
--------
>>> my_instance = MyClass(42)
>>> my_instance.x
42
>>> another_instance = MyClass(43)
>>> another_instance.x
42

Note that values set in subsequent calls to `__init__` will have no
effect on the attribute.  To change the attribute do so on any of
the instances:

>>> another_instance.x = 43
>>> my_instance.x
43
>>> my_instance.x = 42
>>> another_instance.x
42

"""
import typing as tp


class Singleton(type):
    """
    Metaclass for singleton objects.
    """
    __instances: tp.Dict[type, tp.Any] = {}

    def __call__(cls: type, *args, **kwargs) -> tp.Any:
        if cls not in cls.__instances:
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance
        return cls.__instances[cls]
