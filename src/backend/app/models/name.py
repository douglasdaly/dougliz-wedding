# -*- coding: utf-8 -*-
"""
Name model.
"""
from typing import Optional
from uuid import UUID

from app.models.base import AppBaseModel


class NameBase(AppBaseModel):
    """
    Base class for Name objects.
    """
    title: Optional[str] = None
    first: str
    middle: Optional[str] = None
    last: str
    suffix: Optional[str] = None
    short: Optional[str] = None


class NameCreate(NameBase):
    """
    Create model for Name objects.
    """
    pass


class NameUpdate(NameBase):
    """
    Update model for Name objects.
    """
    first: Optional[str] = None
    last: Optional[str] = None


class NameInDBBase(NameBase):
    """
    Database base class for Name objects.
    """
    uid: UUID = None

    class Config:
        orm_mode = True


class Name(NameInDBBase):
    """
    Get model for Name objects.
    """
    pass


class NameInDB(NameInDBBase):
    """
    Database model for Name objects.
    """
    id: int
