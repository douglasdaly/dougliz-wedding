# -*- coding: utf-8 -*-
"""
Permission specification object storage repository.
"""
from abc import ABCMeta

from app.crud.base import Repository
from app.crud.base import T
from app.models.config.permission import PermissionCreate
from app.models.config.permission import PermissionUpdate


class PermissionRepository(
    Repository[T, PermissionCreate, PermissionUpdate],
    metaclass=ABCMeta
):
    """
    Permission specfication object repository base class.
    """
    pass
