# -*- coding: -*-
"""
Configuration Setting model.
"""
import typing as tp
from uuid import UUID

from app.models.base import AppGenericModel


DataT = tp.TypeVar('DataT', (str, int, float, bool))


class SettingBase(AppGenericModel, tp.Generic[DataT]):
    """
    Base model for settings.
    """
    name: str
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
    value: tp.Optional[DataT]


class SettingInDBBase(SettingBase):
    """
    Storage base class for Setting objects.
    """
    uid: UUID = None

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
