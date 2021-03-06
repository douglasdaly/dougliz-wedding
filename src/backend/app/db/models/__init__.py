# -*- coding: utf-8 -*-
"""
Database storage models for the backend API.
"""
from app.db.models.address import Address
from app.db.models.contact_info import ContactInfo
from app.db.models.event import Event
from app.db.models.name import Name
from app.db.models.person import Person
from app.db.models.user import User

from app.db.models import config
from app.db.models import wedding

__all__ = [
    'Address',
    'config',
    'ContactInfo',
    'Event',
    'Name',
    'Person',
    'User',
    'wedding',
]
