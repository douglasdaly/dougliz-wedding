# -*- coding: utf-8 -*-
"""
Address repository.
"""
from app.crud.base import Repository
from app.crud.base import T
from app.models.address import AddressCreate
from app.models.address import AddressUpdate


class AddressRepository(Repository[T, AddressCreate, AddressUpdate]):
    """
    Abstract base Address object repository.
    """
    pass
