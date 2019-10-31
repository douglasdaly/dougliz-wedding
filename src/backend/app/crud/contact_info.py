# -*- coding: utf-8 -*-
"""
ContactInfo object storage repository.
"""
from abc import ABCMeta

from app.crud.base import Repository
from app.crud.base import T
from app.models.contact_info import ContactInfoCreate
from app.models.contact_info import ContactInfoUpdate


class ContactInfoRepository(
    Repository[T, ContactInfoCreate, ContactInfoUpdate],
    metaclass=ABCMeta
):
    """
    Abstract base ContactInfo object storage repository.
    """
    pass
