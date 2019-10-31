# -*- coding: utf-8 -*-
"""
Name repository.
"""
from app.crud.name import NameRepository
from app.db.crud.base import SQLRepositoryMixin
from app.db.models.name import Name


class NameSQLRepository(SQLRepositoryMixin, NameRepository[Name]):
    """
    Name object storage repository.
    """
    __obj_cls__ = Name
