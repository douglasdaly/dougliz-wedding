# -*- coding: utf-8 -*-
"""
Contact information database storage.
"""
from enum import IntEnum
import uuid

import sqlalchemy as sa

from app.db.base_class import Base
from app.db.types import GUID


class PreferredMethod(IntEnum):
    PHONE = 1
    CELL = 2
    EMAIL = 3
    OTHER = 4

    @property
    def field(self) -> str:
        """str: Field name associated with the enum type."""
        if self.value == self.EMAIL.value:
            return 'email_address'
        elif self.value == self.CELL.value:
            return 'cell_phone'
        elif self.value == self.OTHER.value:
            return 'other_type'
        return self.name.lower()


class ContactInfo(Base):
    """
    Database storage specification for Address objects.
    """
    __tablename__ = "contact_info"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    uid = sa.Column(GUID, unique=True, index=True, default=uuid.uuid4)

    name = sa.Column(sa.String)
    phone = sa.Column(sa.String)
    cell_phone = sa.Column(sa.String)
    email_address = sa.Column(sa.String, nullable=False)
    other_type = sa.Column(sa.String)
    other_value = sa.Column(sa.String)
    preferred_method = sa.Column(sa.Enum(PreferredMethod), nullable=False)
