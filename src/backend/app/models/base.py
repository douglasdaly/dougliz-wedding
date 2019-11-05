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
from pydantic.generics import GenericModel
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


class AppGenericModel(GenericModel):
    """
    Base model class for application generic models.
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


def get_custom_getter(
    cls_or_dict: tp.Union[
        tp.Type[BaseModel], tp.Type[GenericModel], tp.Dict[str, str]
    ],
    name: tp.Optional[str] = None
) -> tp.Type[GetterDict]:
    """Gets a new, custom getter dict for doing ORM field mappings.

    Parameters
    ----------
    cls_or_dict : Union[Type[BaseModel] Type[GenericModel], Dict[str, str]]
        The model class (with configured aliases) or the dictionary of
        aliases to use for a new, custom :obj:`GetterDict` class.
    name : str, optional
        The name to use for the new class (if not given one will be
        created from either the `cls_or_dict` class name or 'Custom'
        followed by 'GetterDict').

    Returns
    -------
    Type[GetterDict]
        A new :obj:`GetterDict` class to use for ORM mappings.

    """
    if isinstance(cls_or_dict, dict):
        name = name or "Custom"
        aliases = cls_or_dict.copy()
    else:
        if not hasattr(cls_or_dict, 'Config') \
                or not hasattr(cls_or_dict.Config, 'fields'):
            raise ValueError("Cannot get field aliases from the given class")
        name = name or cls_or_dict.__name__
        aliases = {v: k for k, v in cls_or_dict.Config.fields.items()}

    return type(
        f"{name}GetterDict",
        (BaseCustomGetterDict,),
        {'_aliases': aliases}
    )
