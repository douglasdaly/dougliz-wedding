# -*- coding: utf-8 -*-
"""
Contact information database storage.
"""
import uuid

import sqlalchemy as sa

from app.db.base_class import Base
from app.db.types import GUID
from app.models.contact_info import PreferredMethod


class ContactInfo(Base):
    """
    Database storage specification for Address objects.
    """
    __tablename__ = "contact_info"

    id = sa.Column(sa.Integer, primary_key=True)
    uid = sa.Column(GUID, unique=True, index=True, default=uuid.uuid4)

    name = sa.Column(sa.String)
    phone = sa.Column(sa.String)
    mobile = sa.Column(sa.String)
    email = sa.Column(sa.String, nullable=False)
    other_type = sa.Column(sa.String)
    other_value = sa.Column(sa.String)
    preferred_method = sa.Column(sa.Enum(PreferredMethod), nullable=False)
