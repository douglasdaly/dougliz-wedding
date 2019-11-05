# -*- coding: utf-8 -*-
"""
Database storage model for Name objects.
"""
import uuid

import sqlalchemy as sa

from app.db.base_class import Base
from app.db.types import GUID


class Name(Base):
    """
    Database storage model for Name objects.
    """
    id = sa.Column(sa.Integer, primary_key=True)
    uid = sa.Column(GUID, unique=True, index=True, default=uuid.uuid4)
    title = sa.Column(sa.String)
    first = sa.Column(sa.String, index=True, nullable=False)
    middle = sa.Column(sa.String)
    last = sa.Column(sa.String, index=True, nullable=False)
    suffix = sa.Column(sa.String)
    short = sa.Column(sa.String)
