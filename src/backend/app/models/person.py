# -*- coding: utf-8 -*-
"""
Person model.
"""
import typing as tp
from uuid import UUID

from pydantic import BaseModel

from app.models.address import Address
from app.models.address import AddressCreate
from app.models.address import AddressUpdate
from app.models.contact_info import ContactInfo
from app.models.contact_info import ContactInfoCreate
from app.models.contact_info import ContactInfoUpdate
from app.models.name import Name
from app.models.name import NameCreate
from app.models.name import NameUpdate


class PersonBase(BaseModel):
    """
    Base class for Person objects.
    """
    name: Name
    contact: ContactInfo
    address: tp.Optional[Address] = None


class PersonCreate(PersonBase):
    """
    Create model for Person objects.
    """
    name: tp.Union[UUID, NameCreate]
    contact: tp.Union[UUID, ContactInfoCreate]
    address: tp.Optional[tp.Union[UUID, AddressCreate]] = None


class PersonUpdate(PersonBase):
    """
    Create model for Person objects.
    """
    name: tp.Optional[tp.Union[UUID, NameUpdate]]
    contact: tp.Optional[tp.Union[UUID, ContactInfoUpdate]] = None
    address: tp.Optional[tp.Union[UUID, AddressCreate, AddressUpdate]] = None


class PersonInDBBase(PersonBase):
    """
    Database base class for Person objects.
    """
    uid: UUID

    class Config:
        orm_mode = True


class Person(PersonInDBBase):
    """
    Get model for Person objects.
    """
    pass


class PersonInDB(PersonInDBBase):
    """
    Database storage model for Person objects.
    """
    id: int
    name_id: int
    contact_id: int
    address_id: tp.Optional[int]
