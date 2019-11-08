# -*- coding: utf-8 -*-
"""
Permission storage repository group.
"""
from app.crud.config.core import ConfigRepositoryGroup
from app.db.crud.base import SQLRepositoryGroupMixin
from app.db.crud.config.permission import PermissionSQLRepository
from app.db.crud.config.setting import SettingSQLRepository
from app.db.crud.config.user import UserPermissionSQLRepository
from app.utils.proputils import lazy_property


class ConfigSQLRepositoryGroup(
    SQLRepositoryGroupMixin,
    ConfigRepositoryGroup
):
    """
    Configuration-related SQL-based repository group.
    """

    @lazy_property
    def permission(self) -> PermissionSQLRepository:
        """PermissionSQLRepository: Permission specification repository.
        """
        return PermissionSQLRepository(
            self._uow, self._session, *self._args, **self._kwargs
        )

    @lazy_property
    def setting(self) -> SettingSQLRepository:
        """SettingSQLRepository: Setting storage repository."""
        return SettingSQLRepository(
            self._uow, self._session, *self._args, **self._kwargs
        )

    @lazy_property
    def user(self) -> UserPermissionSQLRepository:
        """UserPermissionSQLRepository: User permissions repository."""
        return UserPermissionSQLRepository(
            self._uow, self._session, *self._args, **self._kwargs
        )
