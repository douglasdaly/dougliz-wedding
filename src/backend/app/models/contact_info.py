# -*- coding: utf-8 -*-
"""
Contact information model.
"""
from typing import Optional
from uuid import UUID

from pydantic import EmailStr

from app.db.models.contact_info import PreferredMethod
from app.models.base import AppBaseModel
from app.models.base import get_custom_getter


class ContactInfoBase(AppBaseModel):
    """
    Base class for ContactInfo objects.
    """
    name: Optional[str] = None
    phone: Optional[str] = None
    mobile: Optional[str] = None
    email: EmailStr
    other_type: Optional[str] = None
    other_value: Optional[str] = None
    preferred_method: PreferredMethod = PreferredMethod.EMAIL

    class Config:
        fields = {
            'other_type': 'otherType',
            'other_value': 'otherValue',
            'preferred_method': 'preferredMethod'
        }


class ContactInfoCreate(ContactInfoBase):
    """
    Create model for ContactInfo objects.
    """
    pass


class ContactInfoUpdate(ContactInfoBase):
    """
    Update model for ContactInfo objects.
    """
    email: Optional[EmailStr] = None
    preferred_method: Optional[PreferredMethod] = None


class ContactInfoInDBBase(ContactInfoBase):
    """
    Database storage base model for ContactInfo objects.
    """
    uid: Optional[UUID] = None

    class Config:
        orm_mode = True
        getter_dict = get_custom_getter(ContactInfoBase)


class ContactInfo(ContactInfoInDBBase):
    """
    Primary model for ContactInfo objects.
    """
    pass


class ContactInfoInDB(ContactInfoInDBBase):
    """
    Database storage model for ContactInfo objects.
    """
    id: int
    preferred_method: int
