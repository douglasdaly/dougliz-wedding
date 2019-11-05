# -*- coding: utf-8 -*-
"""
Configuration Permission model.
"""
import typing as tp
from uuid import UUID

from app.models.config.base import PermissionModelBase
from app.models.config.base import PermissionModelCreateMixin
from app.models.config.base import PermissionModelUpdateMixin
from app.models.config.permission import Permission
from app.models.user import User


class UserPermissionBase(PermissionModelBase):
    """
    Base model for User Permission instances.
    """
    permission: Permission
    user: User


class UserPermissionCreate(PermissionModelCreateMixin, UserPermissionBase):
    """
    User Permission instance creation model.
    """
    read: tp.Optional[bool] = True


class UserPermissionUpdate(PermissionModelUpdateMixin, UserPermissionBase):
    """
    User Permission instance update model.
    """
    pass


class UserPermissionInDBBase(UserPermissionBase):
    """
    Storage base class for User Permission instance objects.
    """
    uid: tp.Optional[UUID] = None

    class Config:
        orm_mode = True


class UserPermission(UserPermissionInDBBase):
    """
    Get model for User Permission instance objects.
    """
    pass


class UserPermissionInDB(UserPermissionInDBBase):
    """
    Storage model for User Permission instance objects.
    """
    id: int
    permission_id: int
    user_id: int
