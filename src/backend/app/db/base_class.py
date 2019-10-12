# -*- coding: utf-8 -*-
"""
Customized declarative base model for SQLAlchemy.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr

from app.utils.strutils import camel_to_snake


class CustomBase(object):
    """
    Customized declarative base with correct table-naming conventions.
    """

    @declared_attr
    def __tablename__(cls) -> str:
        return camel_to_snake(cls.__name__) + 's'


Base = declarative_base(cls=CustomBase)
