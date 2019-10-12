# -*- coding: utf-8 -*-
"""
ContactInfo object storage repository.
"""
from app.crud.contact_info import ContactInfoRepository
from app.db.crud.base import SQLRepository
from app.db.models.contact_info import ContactInfo
from app.models.contact_info import ContactInfoCreate
from app.models.contact_info import ContactInfoUpdate


class ContactInfoSQLRepository(
    SQLRepository[ContactInfo, ContactInfoCreate, ContactInfoUpdate],
    ContactInfoRepository[ContactInfo]
):
    """
    ContactInfo object storage repository.
    """
    __obj_cls__ = ContactInfo
