# -*- coding: utf-8 -*-
"""
Database backend-agnostic GUID column type.
"""
import uuid

from sqlalchemy.types import CHAR
from sqlalchemy.types import TypeDecorator
from sqlalchemy.dialects.postgresql import UUID


class GUID(TypeDecorator):
    """
    Platform-independent GUID type.
    """
    impl = CHAR

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        if not isinstance(value, uuid.UUID):
            return uuid.UUID(value).hex
        else:
            return value.hex

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        if not isinstance(value, uuid.UUID):
            value = uuid.UUID(value)
        return value
