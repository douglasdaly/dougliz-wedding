# -*- coding: utf-8 -*-
"""
Database storage model for User objects.
"""
import sqlalchemy as sa

from app.db.base_class import Base


class User(Base):
    """
    Database storage model for User objects.
    """
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.String, index=True)
    email = sa.Column(sa.String, unique=True, index=True)
    hashed_password = sa.Column(sa.String)
    is_active = sa.Column(sa.Boolean(), default=True)
    is_superuser = sa.Column(sa.Boolean(), default=False)
