# -*- coding: utf-8 -*-
"""
Permission specification object storage repository.
"""
from abc import ABCMeta

from app.crud.base import Repository
from app.crud.base import T
from app.models.config.user import UserPermissionCreate
from app.models.config.user import UserPermissionUpdate


class UserPermissionRepository(
    Repository[T, UserPermissionCreate, UserPermissionUpdate],
    metaclass=ABCMeta
):
    """
    User Permission object repository base class.
    """
    pass
