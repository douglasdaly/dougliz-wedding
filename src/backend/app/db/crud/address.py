# -*- coding: utf-8 -*-
"""
Address repository.
"""
from app.crud.address import AddressRepositoryMixin
from app.db.crud.base import SQLRepository
from app.db.models.address import Address
from app.models.address import AddressCreate
from app.models.address import AddressUpdate


class AddressSQLRepository(
    AddressRepositoryMixin[Address],
    SQLRepository[Address, AddressCreate, AddressUpdate]
):
    """
    SQL-based Address object repository.
    """
    __obj_cls__ = Address
