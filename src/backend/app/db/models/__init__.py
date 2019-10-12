# -*- coding: utf-8 -*-
"""
Database storage models for the backend API.
"""
from app.db.models.address import Address
from app.db.models.contact_info import ContactInfo
from app.db.models.name import Name
from app.db.models.person import Person
from app.db.models.user import User

__all__ = [
    'Address',
    'ContactInfo',
    'Name',
    'Person',
    'User',
]
