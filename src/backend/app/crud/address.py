# -*- coding: utf-8 -*-
"""
Address repository.
"""
import typing as tp

from app.crud.base import Repository
from app.crud.base import T
from app.models.address import AddressCreate
from app.models.address import AddressUpdate


class AddressRepositoryMixin(tp.Generic[T]):
    """
    Address object repository mixin.
    """
    pass


class AddressRepository(
    AddressRepositoryMixin[T], Repository[T, AddressCreate, AddressUpdate]
):
    """
    Abstract base Address object repository.
    """
    pass
