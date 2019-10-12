# -*- coding: utf-8 -*-
"""
Address model.
"""
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class AddressBase(BaseModel):
    """
    Base class for Address objects.
    """
    name: Optional[str] = None
    line_1: str
    line_2: Optional[str] = None
    line_3: Optional[str] = None
    city: str
    state: Optional[str] = None
    zip_code: Optional[int] = None
    country: Optional[str] = None


class AddressCreate(AddressBase):
    """
    Create model for Address objects.
    """
    pass


class AddressUpdate(AddressBase):
    """
    Update model for Address objects.
    """
    line_1: Optional[str] = None
    city: Optional[str] = None


class AddressInDBBase(AddressBase):
    """
    Database base class for Address objects.
    """
    uid: UUID = None

    class Config:
        orm_mode = True


class Address(AddressInDBBase):
    """
    Get model for Address objects.
    """
    pass


class AddressInDB(AddressInDBBase):
    """
    Database model for Address objects.
    """
    id: int
