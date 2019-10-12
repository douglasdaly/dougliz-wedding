# -*- coding: utf-8 -*-
"""
Database storage model for User objects.
"""
import uuid

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.types import GUID


class User(Base):
    """
    Database storage model for User objects.
    """
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    uid = sa.Column(GUID, unique=True, index=True, default=uuid.uuid4)

    person_id = sa.Column(sa.Integer, sa.ForeignKey('people.id'))
    person = relationship("Person")

    email = sa.Column(sa.String, unique=True, index=True)
    hashed_password = sa.Column(sa.String)

    is_active = sa.Column(sa.Boolean(), default=True)
    is_poweruser = sa.Column(sa.Boolean(), default=False)
    is_superuser = sa.Column(sa.Boolean(), default=False)
