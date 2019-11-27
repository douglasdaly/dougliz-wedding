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

    @declared_attr
    def __mapper_args__(cls) -> tp.Dict[str, tp.Any]:
        return {
            'polymorphic_on': 'type',
        }

    @declared_attr
    def id(cls) -> sa.Column:
        return sa.Column(sa.Integer, primary_key=True)

    @declared_attr
    def uid(cls) -> sa.Column:
        return sa.Column(GUID, unique=True, index=True, default=uuid4)

    @declared_attr
    def name(cls) -> sa.Column:
        return sa.Column(sa.String, unique=True, index=True)

    @declared_attr
    def required(cls) -> sa.Column:
        return sa.Column(sa.Boolean, default=False, nullable=False)

    @declared_attr
    def type(cls) -> sa.Column:
        return sa.Column(sa.Enum(ValueType), nullable=False)


class SettingString(Setting):
    """
    String-valued setting.
    """
    id = sa.Column(sa.Integer, sa.ForeignKey('config.settings.id'),
                   primary_key=True)

    @declared_attr
    def value(cls) -> sa.Column:
        return sa.Column(sa.String)

    @declared_attr
    def __mapper_args__(cls) -> tp.Dict[str, tp.Any]:
        return {
            'polymorphic_identity': ValueType.STRING,
        }


class SettingInteger(Setting):
    """
    Integer-valued setting.
    """
    id = sa.Column(sa.Integer, sa.ForeignKey('config.settings.id'),
                   primary_key=True)

    @declared_attr
    def value(cls) -> sa.Column:
        return sa.Column(sa.Integer)

    @declared_attr
    def __mapper_args__(cls) -> tp.Dict[str, tp.Any]:
        return {
            'polymorphic_identity': ValueType.INTEGER,
        }


class SettingFloat(Setting):
    """
    Float-valued setting.
    """
    id = sa.Column(sa.Integer, sa.ForeignKey('config.settings.id'),
                   primary_key=True)

    @declared_attr
    def value(cls) -> sa.Column:
        return sa.Column(sa.Float)

    @declared_attr
    def __mapper_args__(cls) -> tp.Dict[str, tp.Any]:
        return {
            'polymorphic_identity': ValueType.FLOAT,
        }


class SettingBoolean(Setting):
    """
    Boolean-valued setting.
    """
    id = sa.Column(sa.Integer, sa.ForeignKey('config.settings.id'),
                   primary_key=True)

    @declared_attr
    def value(cls) -> sa.Column:
        return sa.Column(sa.Boolean)

    @declared_attr
    def __mapper_args__(cls) -> tp.Dict[str, tp.Any]:
        return {
            'polymorphic_identity': ValueType.BOOLEAN,
        }


class SettingDatetime(Setting):
    """
    Datetime-valued setting.
    """
    id = sa.Column(sa.Integer, sa.ForeignKey('config.settings.id'),
                   primary_key=True)

    @declared_attr
    def value(cls) -> sa.Column:
        return sa.Column(sa.DateTime)

    @declared_attr
    def __mapper_args__(cls) -> tp.Dict[str, tp.Any]:
        return {
            'polymorphic_identity': ValueType.DATETIME,
        }


class SettingUUID(Setting):
    """
    UUID-valued setting.
    """
    id = sa.Column(sa.Integer, sa.ForeignKey('config.settings.id'),
                   primary_key=True)

    @declared_attr
    def value(cls) -> sa.Column:
        return sa.Column(GUID)

    @declared_attr
    def __mapper_args__(cls) -> tp.Dict[str, tp.Any]:
        return {
            'polymorphic_identity': ValueType.UUID,
        }
