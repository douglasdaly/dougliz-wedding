# -*- coding: utf-8 -*-
# NOTE: ``getter_dict`` and ``_decompose_class`` not implemented in
#   versions < 1.0 of pydantic.  The correct conversion of database
#   classes with aliased fields requires this.  If using pydantic < 1.0
#   be sure to apply the appropriate monkey-patch.
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
    _aliases: tp.Mapping[str, str]

    def get(self, key: tp.Any, default: tp.Any) -> tp.Any:
        return super().get(self._aliases.get(key, key), default)


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
    aliases = {v: k for k, v in cls.Config.fields.items()}
    return type(
        f"{cls.__name__}GetterDict",
        (BaseCustomGetterDict,),
        {'_aliases': aliases}
    )
