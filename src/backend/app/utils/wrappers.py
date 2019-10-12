# -*- coding: utf-8 -*-
"""
Base components for wrappers.
"""
from abc import ABC
import functools
import inspect
from types import FunctionType
from types import MethodType
from types import ModuleType
import typing as tp


Wrappable = tp.TypeVar('Wrappable', ModuleType, type, object)


class WrapperInjector(ABC):
    """
    Groups a module's functions into a single class with parameter
    injection.

    Parameters
    ----------
    *args : tuple, optional
        Arguments to partially-wrap each module function with.
    **kwargs : Mapping[str, Any], optional
        Keyword arguments to partially-wrap each module function with.

    """

    def __init__(self, *args, **kwargs) -> None:
        self._args = args
        self._kwargs = kwargs
        return

    @classmethod
    def __wrap_function(cls, func: tp.Callable) -> tp.Callable:
        """Creates a wrapper function which injects object parameters.

        This is used to wrap functions defined in other modules into
        this class with parameters stored in this instance injected into
        the wrapped `func` prior to any additional parameters.  This is
        done in two parts:

            1. Create a new ``partial`` with this classes ``self._args``
               and ``self._kwargs``.
            2. Run that new ``partial`` from the first step with any
               additional ``args`` or ``kwargs`` passed in.

        Parameters
        ----------
        func : Callable
            The function to wrap for calls from this class.

        Returns
        -------
        Callable
            The wrapped/adapted function to use.

        """
        @functools.wraps(func)
        def _function_wrapper(self, *args, **kwargs) -> tp.Any:
            p = functools.partial(func, *self._args, **self._kwargs)
            return p(*args, **kwargs)

        return _function_wrapper

    @classmethod
    def __wrap_method(cls, meth: tp.Callable) -> tp.Callable:
        """Creates a wrapper method which injects object parameters.

        This is used to wrap methods defined in other classes into
        this class with parameters stored in this instance injected into
        the wrapped `meth` prior to any additional parameters.  This is
        done in two parts:

            1. Create a new ``partialmethod`` with this classes
               ``self._args`` and ``self._kwargs``.
            2. Run that new ``partialmethod`` from the first step with
               any additional ``args`` or ``kwargs`` passed in.

        Parameters
        ----------
        meth : Callable
            The method to wrap for calls from this class.

        Returns
        -------
        Callable
            The wrapped/adapted method to use.

        """
        @functools.wraps(meth)
        def _method_wrapper(self, *args, **kwargs) -> tp.Any:
            p = functools.partialmethod(meth, *self._args, **self.__kwargs)
            return p(*args, **kwargs)

        return _method_wrapper


def _make_decorator(
    obj: Wrappable,
    to_wrap: tp.Iterable[str]
) -> tp.Callable[[tp.Type[WrapperInjector]], tp.type[WrapperInjector]]:
    """Makes the decorator function to use for wrapping.

    Parameters
    ----------
    obj : :obj:`ModuleType`, :obj:`type` or :obj:`object`
        The source object to wrap the `to_wrap` attributes of.
    to_wrap : Iterable[str]
        The names of the attributes of `obj` to wrap.

    Returns
    -------
    Callable[[Type[WrapperInjector]], Type[WrapperInjector]]
        The decorator to use for wrapping a new :obj:`WrapperInjector`
        class.

    """
    def _wrapper(cls: tp.Type[WrapperInjector]) -> tp.Type[WrapperInjector]:
        cls.__wrapped__ = tuple(to_wrap)
        to_wrap = {x: getattr(obj, x) for x in to_wrap}
        for k, v in to_wrap.items():
            if isinstance(v, FunctionType):
                setattr(cls, k, cls.__wrap_function(v))
            else:
                setattr(cls, k, cls.__wrap_method(v))
        return cls

    return _wrapper


def _get_default_class_exports(cls: type) -> tp.List[str]:
    """Gets the wrappable functions of the given `cls`."""
    def _filter_instance_methods(x: tp.Callable):
        if isinstance(x, MethodType):
            return True
        f_sig = inspect.signature(x)
        if len(f_sig.parameters) > 0:
            p_1 = next(iter(f_sig.parameters.values()))
            return p_1.name != 'self'
        return True

    return [
        x for x in _get_default_object_exports(cls)
        if _filter_instance_methods(x)
    ]


def _get_default_module_exports(module: ModuleType) -> tp.List[str]:
    """Gets the wrappable functions of the given `module`."""
    if hasattr(module, '__all__'):
        return module.__all__

    rv = []
    for k, v in module.__dict__.items():
        if k.startswith('_') or not callable(v):
            continue
        if inspect.getmodule(v) == module:
            rv.append(k)
    return rv


def _get_default_object_exports(obj: tp.Union[type, object]) -> tp.List[str]:
    """Gets the wrappable method names from the given `obj`."""
    rv = []
    for k, v in inspect.getmembers(obj, callable):
        if k.startswith('_'):
            continue
        rv.append(k)
    return rv


def get_wrappable_items(
    obj: Wrappable,
    include: tp.Optional[tp.Iterable[str]] = None,
    exclude: tp.Optional[tp.Iterable[str]] = None
) -> tp.Iterable[str]:
    """Gets the wrappable items from the `obj` to wrap.

    Parameters
    ----------
    obj : Wrappable
        The object to get the wrappable elements of.
    include : Iterable[str], optional
        The :obj:`callable` elements of the given `obj` to wrap (if
        ``None`` then all callable elements which are on the given `obj`
        will be used).
    exclude : Iterable[str], optional
        The :obj:`callable` elements of the given `obj` to ignore.

    Returns
    -------
    Iterable[str]
        The names of the wrappable elements to export from the given
        `obj` and `include`/`exclude` constraints.

    Raises
    ------
    AttributeError
        If an element to be wrapped (as specified by `include`) doesn't
        exist on the given `obj`.
    ValueError
        If an element to be wrapped from the given `obj` is not
        :obj:`callable`.

    """
    rv = []
    if not include:
        if isinstance(obj, ModuleType):
            rv = _get_default_module_exports(obj)
        elif isinstance(obj, type):
            rv = _get_default_class_exports(obj)
        else:
            rv = _get_default_object_exports(obj)
    else:
        rv.extend(include)
    if exclude:
        rv = [x for x in rv if x not in exclude]

    for nm in rv:
        elem = getattr(obj, nm)
        if not callable(elem):
            raise ValueError(f"Not callable: {elem!r}")
    return rv


def module_wrapper(
    module: ModuleType,
    include: tp.Optional[tp.Iterable[str]] = None,
    exclude: tp.Optional[tp.Iterable[str]] = None
) -> tp.Callable[[tp.Type[WrapperInjector]], tp.Type[WrapperInjector]]:
    """Decorator for exporting module functions.

    To use this, suppose we have a module containing similar functions
    for working with our database to manage data.  Suppose the module
    interacts with the database for information about people:

    .. code-block:: python

        # person.py - for working with people data in the database

        def add(db, first_name, last_name):
            ...

        def update(db, first_name, last_name):
            ...

        def remove(db, first_name, last_name):
            ...

    Now we want to be able to call these functions from another class
    (such as a Unit of Work implementation) and inject the ``db`` into
    the functions.  We could wrap this module and then in the new
    :obj:`ModuleWrapper` class inject the same ``db`` into each call:

    .. code-block:: python

        # person_wrapper.py - a class to wrap person.py functions

        from wrappers import WrapperInject
        from wrappers import module_wrapper

        import person


        @module_wrapper(person)
        class PersonWrapper(WrapperInject):
            pass

    Now, in our unit of work class (or whatever else needs to have this
    "bundle" of functions):

    .. code-block:: python

        # unit_of_work.py - Unit of work for database operations

        from .person_wrapper import PersonWrapper

        class UnitOfWork(object):

            def __init__(self, db):
                self._db = db
                return

            @property
            def people(self):
                return PersonWrapper(self._db)

            ...

    Then using this unit of work becomes very simple:

    .. code-block:: python

        with UnitOfWork(db_connection) as uow:
            uow.people.add('John', 'Doe')


    Parameters
    ----------
    module : ModuleType
        The python module to wrap with the decorated class.
    include : Iterable[str], optional
        The :obj:`callable` attributes of the given `module` to wrap (if
        ``None`` then all callables which are defined *in* the given
        `module` will be used).
    exclude : Iterable[str], optional
        The :obj:`callable` attributes of the given `module` to ignore
        when performing the wrapping.

    Returns
    -------
    Callable[[Type[WrapperInjector]], Type[WrapperInjector]]
        The decorator, tailored for the given model, which will add the
        specified functions to the wrapped class.

    Raises
    ------
    ValueError
        If an attribute being wrapped from the given `module` is not a
        :obj:`callable`.

    """
    to_wrap = get_wrappable_items(module, include=include, exclude=exclude)
    return _make_decorator(module, to_wrap)


def class_wrapper(
    cls: type,
    include: tp.Optional[tp.Iterable[str]] = None,
    exclude: tp.Optional[tp.Iterable[str]] = None
) -> tp.Callable[[tp.Type[WrapperInjector]], tp.Type[WrapperInjector]]:
    """Wraps the given `cls` type."""
    to_wrap = get_wrappable_items(cls, include=include, exclude=exclude)
    return _make_decorator(cls, to_wrap)


def object_wrapper(
    obj: object,
    include: tp.Optional[tp.Iterable[str]] = None,
    exclude: tp.Optional[tp.Iterable[str]] = None
) -> tp.Callable[[tp.Type[WrapperInjector]], tp.Type[WrapperInjector]]:
    """Wraps the given `obj` object instance."""
    to_wrap = get_wrappable_items(obj, include=include, exclude=exclude)
    return _make_decorator(obj, to_wrap)
