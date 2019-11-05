# -*- coding: utf-8 -*-
"""
Database storage specification for User Permission instance objects.
"""
import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.models.permissions.base import PermissionMixin


class UserPermission(PermissionMixin, Base):
    """
    Database storage specification for Address objects.
    """
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'),
                        primary_key=True)
    user = relationship("User")
