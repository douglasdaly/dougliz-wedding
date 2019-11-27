# -*- coding: utf-8 -*-
"""
Configuration Setting model.
"""
from datetime import datetime
from enum import IntEnum
import typing as tp
from uuid import UUID

from app.models.base import AppBaseModel


DataT = tp.TypeVar('DataT', float, int, bool, datetime, UUID, str)


class ValueType(IntEnum):
    """
    Type-identifier for setting types.
    """
    STRING = 1
    INTEGER = 2
    FLOAT = 3
    BOOLEAN = 4
    DATETIME = 5
    UUID = 6

    @classmethod
    def from_object(cls, value: DataT) -> 'ValueType':
        """Maps the given value to the correct enumeration value.

        Parameters
        ----------
        value : DataT
            The object to map.

        Returns
        -------
        ValueType
            The associated enumeration value for the given `value`.

        Raises
        ------
        NotImplementedError
            If the given `value` object's type is not implemented.

        """
        return cls.from_type(type(value))

    @classmethod
    def from_type(cls, value: tp.Type[DataT]) -> 'ValueType':
        """Maps the given type to the correct enumeration value.

        Parameters
        ----------
        value : type
            The type to map.

        Returns
        -------
        ValueType
            The associated enumeration value for the given `value`.

        Raises
        ------
        NotImplementedError
            If the given `value` type is not implemented.

        """
        if value == str:
            return cls.STRING
        elif value == int:
            return cls.INTEGER
        elif value == float:
            return cls.FLOAT
        elif value == bool:
            return cls.BOOLEAN
        elif value == datetime:
            return cls.DATETIME
        elif value == UUID:
            return cls.UUID
        raise NotImplementedError(value)


class SettingBase(AppBaseModel):
    """
    Base model for settings.
    """
    name: str
    required: bool = False
    value: tp.Optional[DataT]
    type: ValueType


class SettingCreate(SettingBase):
    """
    Setting creation model.
    """
    type: tp.Optional[ValueType]


class SettingUpdate(SettingBase):
    """
    Setting update model.
    """
    name: tp.Optional[str]
    required: tp.Optional[bool]
    type: tp.Optional[ValueType]


class SettingInDBBase(SettingBase):
    """
    Storage base class for Setting objects.
    """
    uid: tp.Optional[UUID] = None

    class Config:
        orm_mode = True


class Setting(SettingInDBBase):
    """
    Get model for Setting objects.
    """
    pass


class SettingInDB(SettingInDBBase):
    """
    Storage model for Setting objects.
    """
    id: int
