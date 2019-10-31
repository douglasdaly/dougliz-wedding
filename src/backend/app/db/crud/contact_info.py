# -*- coding: utf-8 -*-
"""
ContactInfo object storage repository.
"""
from app.crud.contact_info import ContactInfoRepository
from app.db.crud.base import SQLRepositoryMixin
from app.db.models.contact_info import ContactInfo


class ContactInfoSQLRepository(
    SQLRepositoryMixin,
    ContactInfoRepository[ContactInfo]
):
    """
    ContactInfo object storage repository.
    """
    __obj_cls__ = ContactInfo
