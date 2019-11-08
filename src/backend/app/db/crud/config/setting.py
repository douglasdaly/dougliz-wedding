# -*- coding: utf-8 -*-
"""
SQL-based configuration Setting storage repository implementation.
"""
from app.crud.config.setting import SettingRepository
from app.db.crud.base import SQLRepositoryMixin
from app.db.models.config.setting import Setting


class SettingSQLRepository(
    SQLRepositoryMixin,
    SettingRepository[Setting]
):
    """
    Setting SQL-based object storage repository.
    """
    __obj_cls__ = Setting

    def get_by_name(self, name: str, *, raise_ex: bool = False) -> Setting:
        return self._session.query(self.__obj_cls__) \
            .filter(self.__obj_cls__.name == name) \
            .first()
