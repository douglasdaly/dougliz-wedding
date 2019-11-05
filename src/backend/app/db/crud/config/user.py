# -*- coding: utf-8 -*-
"""
User Permission settings SQL-based object repository.
"""
from app.crud.config.user import UserPermissionRepository
from app.db.crud.base import SQLRepositoryMixin
from app.db.models.config.user import UserPermission


class UserPermissionSQLRepository(
    SQLRepositoryMixin,
    UserPermissionRepository[UserPermission]
):
    """
    User Permission SQL-based object storage repository.
    """
    __obj_cls__ = UserPermission
