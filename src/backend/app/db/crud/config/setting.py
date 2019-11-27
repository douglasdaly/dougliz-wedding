# -*- coding: utf-8 -*-
"""
SQL-based configuration Setting storage repository implementation.
"""
from app.crud.config.setting import SettingRepository
from app.db.crud.base import SQLRepositoryMixin
from app.db.models.config.setting import Setting
from app.db.models.config.setting import (
    SettingBoolean,
    SettingDatetime,
    SettingFloat,
    SettingInteger,
    SettingString,
    SettingUUID,
)
from app.models.config.setting import SettingCreate
from app.models.config.setting import ValueType


_type_mapping = {
    ValueType.BOOLEAN: SettingBoolean,
    ValueType.DATETIME: SettingDatetime,
    ValueType.FLOAT: SettingFloat,
    ValueType.INTEGER: SettingInteger,
    ValueType.STRING: SettingString,
    ValueType.UUID: SettingUUID,
}


class SettingSQLRepository(
    SQLRepositoryMixin,
    SettingRepository[Setting]
):
    """
    Setting SQL-based object storage repository.
    """
    __obj_cls__ = Setting

    def _create_obj(self, obj: SettingCreate) -> Setting:
        return _type_mapping[obj.type](**dict(obj))

    def get_by_name(self, name: str, *, raise_ex: bool = False) -> Setting:
        return self._session.query(self.__obj_cls__) \
            .filter(self.__obj_cls__.name == name) \
            .first()
