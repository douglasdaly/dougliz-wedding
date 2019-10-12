# -*- coding: utf-8 -*-
"""
Base model class.
"""
import typing as tp

import orjson
from pydantic import BaseModel
from pydantic.utils import GetterDict


def orjson_dumps(v: tp.Any, *, default: tp.Optional[tp.Callable]) -> str:
    """Convert the returned bytes back to string."""
    return orjson.dumps(v, default=default).decode()


class AppBaseModel(BaseModel):
    """
    Base model class for application models.
    """

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class BaseCustomGetterDict(GetterDict):
    """
    Base custom getter dict class.
    """
    __aliases: tp.Mapping[str, str]

    def __getitem__(self, key: str) -> tp.Any:
        return super().__getitem__(self.__aliases.get(key, key))

    def get(self, key: tp.Any, default: tp.Any = None) -> tp.Any:
        return super().get(self.__aliases.get(key, key), default=default)

    def __iter__(self) -> tp.Iterator[str]:
        for name in dir(self._obj):
            if not name.startswith('_'):
                yield self.__aliases.get(name, name)


def get_custom_getter(cls: tp.Type[BaseModel]) -> tp.Type[GetterDict]:
    """Gets a new, custom getter dict for doing ORM field mappings.

    Parameters
    ----------
    cls : Type[BaseModel]
        The model class (with configured aliases) to get a new, custom
        :obj:`GetterDict` for.

    Returns
    -------
    Type[GetterDict]
        A new :obj:`GetterDict` class to use for ORM mappings.

    """
    if not hasattr(cls, 'Config') or not hasattr(cls.Config, 'fields'):
        raise ValueError("Cannot get field aliases from the given class")
    aliases = cls.Config.fields.copy()

    class _NewGetterDict(BaseCustomGetterDict):
        __aliases = aliases
        __name__ = f"{cls.__name__}GetterDict"

    return _NewGetterDict
