# -*- coding: utf-8 -*-
"""
Configuration Setting model.
"""
from datetime import datetime
from enum import IntEnum
import typing as tp
from uuid import UUID

from app.models.base import AppGenericModel


DataT = tp.TypeVar('DataT', str, int, float, bool, datetime)


class ValueType(IntEnum):
    """
    Type-identifier for setting types.
    """
    STRING = 1
    INTEGER = 2
    FLOAT = 3
    BOOLEAN = 4
    DATETIME = 5


class SettingBase(AppGenericModel, tp.Generic[DataT]):
    """
    Base model for settings.
    """
    name: str
    required: bool = False
    value: tp.Optional[DataT]


class SettingCreate(SettingBase):
    """
    Setting creation model.
    """
    pass


class SettingUpdate(SettingBase):
    """
    Setting update model.
    """
    name: tp.Optional[str]
    required: tp.Optional[bool]


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
    type: ValueType
