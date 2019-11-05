# -*- coding: utf-8 -*-
"""
Database storage specification for Permission objects.
"""
import uuid

import sqlalchemy as sa

from app.db.base_class import Base
from app.db.models.permissions.base import PermissionSchemaMixin
from app.db.types import GUID


class Permission(PermissionSchemaMixin, Base):
    """
    Database storage specification for Address objects.
    """
    id = sa.Column(sa.Integer, primary_key=True)
    uid = sa.Column(GUID, unique=True, index=True, default=uuid.uuid4)

    name = sa.Column(sa.String, index=True, unique=True)
    description = sa.Column(sa.Text)
    create_default: sa.Column(sa.Boolean, nullable=False)
    read_default: sa.Column(sa.Boolean, nullable=False)
    update_default: sa.Column(sa.Boolean, nullable=False)
    delete_default: sa.Column(sa.Boolean, nullable=False)
