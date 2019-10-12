# -*- coding: utf-8 -*-
"""
Database storage model for Address objects.
"""
import uuid

import sqlalchemy as sa

from app.db.base_class import Base
from app.db.types import GUID


class Address(Base):
    """
    Database storage specification for Address objects.
    """
    __tablename__ = "addresses"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    uid = sa.Column(GUID, unique=True, index=True, default=uuid.uuid4)

    name = sa.Column(sa.String)
    line_1 = sa.Column(sa.String, nullable=False)
    line_2 = sa.Column(sa.String)
    line_3 = sa.Column(sa.String)
    city = sa.Column(sa.String, nullable=False)
    state = sa.Column(sa.String)
    zip_code = sa.Column(sa.SmallInteger)
    country = sa.Column(sa.String)
