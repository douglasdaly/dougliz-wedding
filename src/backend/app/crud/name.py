# -*- coding: utf-8 -*-
"""
Name repository.
"""
from app.crud.base import Repository
from app.crud.base import T
from app.models.name import NameCreate
from app.models.name import NameUpdate


class NameRepository(Repository[T, NameCreate, NameUpdate]):
    """
    Abstract base Name object storage repository.
    """
    pass
