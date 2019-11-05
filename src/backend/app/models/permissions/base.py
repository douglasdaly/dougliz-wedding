# -*- coding: utf-8 -*-
"""
Base classes for Permission objects.
"""
from abc import ABC
import typing as tp

from app.models.base import AppBaseModel


class PermissionModelBase(AppBaseModel, ABC):
    """
    Abstract base class for Permission instance objects.
    """
    create: bool
    read: bool
    update: bool
    delete: bool


class PermissionModelCreateMixin(ABC):
    """
    Abstract base create mixin class for Permission objects.
    """
    create: tp.Optional[bool] = False
    read: tp.Optional[bool] = False
    update: tp.Optional[bool] = False
    delete: tp.Optional[bool] = False


class PermissionModelUpdateMixin(ABC):
    """
    Abstract base update mixin class for Permission objects.
    """
    create: tp.Optional[bool]
    read: tp.Optional[bool]
    update: tp.Optional[bool]
    delete: tp.Optional[bool]
