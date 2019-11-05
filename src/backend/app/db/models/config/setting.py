# -*- coding: utf-8 -*-
"""
Database storage models for Setting objects.
"""
import typing as tp
from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declared_attr

from app.db.base_class import Base
from app.db.models.config.base import ConfigSchemaMixin
from app.db.types.guid import GUID
from app.models.config.setting import ValueType


class Setting(ConfigSchemaMixin, Base):
    """
    Base class for setting storage.
    """
    __abstract__ = True
    __mapper_args__: tp.Dict[str, tp.Any] = {
        'polymorphic_on': 'type',
    }

    id = sa.Column(sa.Integer, primary_key=True)
    uid = sa.Column(GUID, unique=True, index=True, default=uuid4)

    name = sa.Column(sa.String, unique=True, index=True)
    required = sa.Column(sa.Boolean, default=False, nullable=False)
    type = sa.Column(sa.Enum(ValueType), nullable=False, index=True)


class StringSetting(Setting):
    """
    String-valued setting.
    """
    value: sa.Column(sa.String)

    @declared_attr
    def __mapper_args__(cls) -> tp.Dict[str, tp.Any]:
        rv = super().__mapper_args__
        rv['polymorphic_identity'] = ValueType.STRING
        return rv


class IntegerSetting(Setting):
    """
    Integer-valued setting.
    """
    value: sa.Column(sa.Integer)

    @declared_attr
    def __mapper_args__(cls) -> tp.Dict[str, tp.Any]:
        rv = super().__mapper_args__
        rv['polymorphic_identity'] = ValueType.INTEGER
        return rv


class FloatSetting(Setting):
    """
    Float-valued setting.
    """
    value: sa.Column(sa.Float)

    @declared_attr
    def __mapper_args__(cls) -> tp.Dict[str, tp.Any]:
        rv = super().__mapper_args__
        rv['polymorphic_identity'] = ValueType.FLOAT
        return rv


class BooleanSetting(Setting):
    """
    Boolean-valued setting.
    """
    value: sa.Column(sa.Boolean)

    @declared_attr
    def __mapper_args__(cls) -> tp.Dict[str, tp.Any]:
        rv = super().__mapper_args__
        rv['polymorphic_identity'] = ValueType.BOOLEAN
        return rv


class DatetimeSetting(Setting):
    """
    Datetime-valued setting.
    """
    value: sa.Column(sa.DateTime)

    @declared_attr
    def __mapper_args__(cls) -> tp.Dict[str, tp.Any]:
        rv = super().__mapper_args__
        rv['polymorphic_identity'] = ValueType.DATETIME
        return rv
