# -*- coding: utf-8 -*-
"""
ContactInfo object storage repository.
"""
from app.crud.base import Repository
from app.crud.base import T
from app.models.contact_info import ContactInfoCreate
from app.models.contact_info import ContactInfoUpdate


class ContactInfoRepository(
    Repository[T, ContactInfoCreate, ContactInfoUpdate]
):
    """
    Abstract base ContactInfo object storage repository.
    """
    pass
