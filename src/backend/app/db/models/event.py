# -*- coding: utf-8 -*-
"""
Person database storage model.
"""
import uuid

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.types import GUID


class Event(Base):
    """
    Database storage for Event objects.
    """
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    uid = sa.Column(GUID, unique=True, index=True, default=uuid.uuid4)

    name = sa.Column(sa.String, nullable=False, index=True)

    date = sa.Column(sa.Date, nullable=False, index=True)
    start = sa.Column(sa.Time)
    end = sa.Column(sa.Time)

    address_id = sa.Column(sa.Integer, sa.ForeignKey('addresses.id'))
    address = relationship("Address")
