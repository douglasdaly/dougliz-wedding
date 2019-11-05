# -*- coding: utf-8 -*-
"""
Permissions model object storage repository group.
"""
from abc import ABCMeta
from abc import abstractmethod

from app.crud.base import RepositoryGroup
from app.crud.config.permission import PermissionRepository
from app.crud.config.user import UserPermissionRepository


class ConfigRepositoryGroup(RepositoryGroup, metaclass=ABCMeta):
    """
    Configuration-related storage repository grouper.
    """

    @property
    @abstractmethod
    def permission(self) -> PermissionRepository:
        """PermissionRepository: Permission specification storage
        repository."""
        pass

    @property
    @abstractmethod
    def user(self) -> UserPermissionRepository:
        """UserPermissionRepository: UserPermission storage repository.
        """
        pass
