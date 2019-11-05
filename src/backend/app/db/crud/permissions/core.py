# -*- coding: utf-8 -*-
"""
Permission storage repository group.
"""
from app.crud.permissions.core import PermissionsRepositoryGroup
from app.db.crud.base import SQLRepositoryGroupMixin
from app.db.crud.permissions.permission import PermissionSQLRepository
from app.db.crud.permissions.user import UserPermissionSQLRepository
from app.utils.proputils import lazy_property


class PermissionsSQLRepositoryGroup(
    SQLRepositoryGroupMixin,
    PermissionsRepositoryGroup
):
    """
    Permissions SQL-based repository group.
    """

    @lazy_property
    def permission(self) -> PermissionSQLRepository:
        """PermissionSQLRepository: Permission specification repository.
        """
        return PermissionSQLRepository(
            self._uow, self._session, *self._args, **self._kwargs
        )

    @lazy_property
    def user(self) -> UserPermissionSQLRepository:
        """UserPermissionSQLRepository: User permissions repository."""
        return UserPermissionSQLRepository(
            self._uow, self._session, *self._args, **self._kwargs
        )
