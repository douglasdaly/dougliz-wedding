# -*- coding: utf-8 -*-
"""
Database storage base specifications for permission objects.
"""
import typing as tp

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship
from sqlalchemy.orm import RelationshipProperty


class ConfigSchemaMixin(object):
    """
    Database storage mixin to put tables in the 'permission' schema.
    """

    @declared_attr
    def __table_args__(cls) -> tp.Dict[str, tp.Any]:
        return {
            'schema': 'config',
        }


class PermissionMixin(ConfigSchemaMixin):
    """
    Database storage mixin for Permission objects.
    """

    @declared_attr
    def permission_id(cls) -> sa.Column:
        return sa.Column(
            sa.Integer,
            sa.ForeignKey('config.permissions.id'),
            primary_key=True
        )

    @declared_attr
    def permission(cls) -> RelationshipProperty:
        return relationship("Permission")

    @declared_attr
    def create(cls) -> sa.Column:
        return sa.Column(sa.Boolean, nullable=False)

    @declared_attr
    def read(cls) -> sa.Column:
        return sa.Column(sa.Boolean, nullable=False)

    @declared_attr
    def update(cls) -> sa.Column:
        return sa.Column(sa.Boolean, nullable=False)

    @declared_attr
    def delete(cls) -> sa.Column:
        return sa.Column(sa.Boolean, nullable=False)
