# -*- coding: utf-8 -*-
"""
Database storage models for permission models.
"""
from app.db.models.permissions.permission import Permission
from app.db.models.permissions.user import UserPermission

__all__ = [
    'Permission',
    'UserPermission',
]
