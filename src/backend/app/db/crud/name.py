# -*- coding: utf-8 -*-
"""
Name repository.
"""
from app.crud.name import NameRepository
from app.db.crud.base import SQLRepository
from app.db.models.name import Name
from app.models.name import NameCreate
from app.models.name import NameUpdate


class NameSQLRepository(
    SQLRepository[Name, NameCreate, NameUpdate],
    NameRepository[Name]
):
    """
    Name object storage repository.
    """
    __obj_cls__ = Name
