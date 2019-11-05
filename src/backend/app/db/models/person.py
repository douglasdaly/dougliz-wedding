# -*- coding: utf-8 -*-
"""
Database storage for Person objects.
"""
import uuid

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.types import GUID


class Person(Base):
    """
    Database storage for Person objects.
    """
    __tablename__ = 'people'

    id = sa.Column(sa.Integer, primary_key=True)
    uid = sa.Column(GUID, unique=True, index=True, default=uuid.uuid4)

    name_id = sa.Column(sa.Integer, sa.ForeignKey('names.id'),
                        nullable=False, unique=True, index=True)
    name = relationship("Name")

    contact_id = sa.Column(sa.Integer, sa.ForeignKey('contact_info.id'),
                           nullable=False)
    contact = relationship("ContactInfo")

    address_id = sa.Column(sa.Integer, sa.ForeignKey('addresses.id'))
    address = relationship("Address")
