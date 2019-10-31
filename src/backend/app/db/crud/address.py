# -*- coding: utf-8 -*-
"""
Address repository.
"""
from app.crud.address import AddressRepository
from app.db.crud.base import SQLRepositoryMixin
from app.db.models.address import Address


class AddressSQLRepository(SQLRepositoryMixin, AddressRepository[Address]):
    """
    SQL-based Address object repository.
    """
    __obj_cls__ = Address
