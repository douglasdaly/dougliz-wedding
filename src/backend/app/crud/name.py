# -*- coding: utf-8 -*-
"""
Name repository.
"""
from abc import ABCMeta
from app.crud.base import Repository
from app.crud.base import T
from app.models.name import NameCreate
from app.models.name import NameUpdate


class NameRepository(Repository[T, NameCreate, NameUpdate], metaclass=ABCMeta):
    """
    Abstract base class for Name object storage repository.
    """
    pass
