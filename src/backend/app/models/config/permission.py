# -*- coding: utf-8 -*-
"""
Permission specification model.
"""
import typing as tp
from uuid import UUID

from app.models.base import AppBaseModel
from app.models.base import get_custom_getter


PermissionT = tp.TypeVar('PermissionT')


class PermissionBase(AppBaseModel):
    """
    Base model for Permissions.
    """
    name: str
    description: tp.Optional[str]
    create_default: bool
    read_default: bool
    update_default: bool
    delete_default: bool

    class Config:
        fields = {
            'create_default': 'createDefault',
            'read_default': 'readDefault',
            'update_default': 'updateDefault',
            'delete_default': 'deleteDefault',
        }


class PermissionCreate(PermissionBase):
    """
    Permission creation model.
    """
    create_default: tp.Optional[bool] = False
    read_default: tp.Optional[bool] = False
    update_default: tp.Optional[bool] = False
    delete_default: tp.Optional[bool] = False


class PermissionUpdate(PermissionBase):
    """
    Permission update model.
    """
    name: tp.Optional[str]
    description: tp.Optional[str]
    create_default: tp.Optional[bool]
    read_default: tp.Optional[bool]
    update_default: tp.Optional[bool]
    delete_default: tp.Optional[bool]


class PermissionInDBBase(PermissionBase):
    """
    Storage base class for Permission objects.
    """
    uid: tp.Optional[UUID] = None

    class Config:
        orm_mode = True
        getter_dict = get_custom_getter(PermissionBase)

    def set_defaults(self, new_perm: PermissionT) -> PermissionT:
        """Sets the default values for the permission object given.

        Parameters
        ----------
        new_perm : PermT
            The new permission object to set default values for create,
            read, update and delete for.

        Returns
        -------
        PermT
            The permission object with the values set to their defaults.

        """
        new_perm.create = self.create_default
        new_perm.read = self.read_default
        new_perm.update = self.update_default
        new_perm.delete = self.delete_default
        return new_perm


class Permission(PermissionInDBBase):
    """
    Read model for Permission objects.
    """
    pass


class PermissionInDB(PermissionInDBBase):
    """
    Storage model for Permission objects.
    """
    id: int
