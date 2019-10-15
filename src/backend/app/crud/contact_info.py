# -*- coding: utf-8 -*-
"""
ContactInfo object storage repository.
"""
import typing as tp

from app.crud.base import Repository
from app.crud.base import T
from app.models.contact_info import ContactInfoCreate
from app.models.contact_info import ContactInfoUpdate


class ContactInfoRepositoryMixin(tp.Generic[T]):
    """
    ContactInfo object repository mixin.
    """
    pass


class ContactInfoRepository(
    ContactInfoRepositoryMixin[T],
    Repository[T, ContactInfoCreate, ContactInfoUpdate]
):
    """
    Abstract base ContactInfo object storage repository.
    """
    pass
