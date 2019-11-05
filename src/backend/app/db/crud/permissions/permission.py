# -*- coding: utf-8 -*-
"""
Permission specification SQL-based object repository.
"""
from app.crud.permissions.permission import PermissionRepository
from app.db.crud.base import SQLRepositoryMixin
from app.db.models.permissions.permission import Permission


class PermissionSQLRepository(
    SQLRepositoryMixin,
    PermissionRepository[Permission]
):
    """
    Permission SQL-based object storage repository.
    """
    __obj_cls__ = Permission
