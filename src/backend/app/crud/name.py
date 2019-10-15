# -*- coding: utf-8 -*-
"""
Name repository.
"""
import typing as tp

from app.crud.base import Repository
from app.crud.base import T
from app.models.name import NameCreate
from app.models.name import NameUpdate


class NameRepositoryMixin(tp.Generic[T]):
    """
    Name object storage repository mixin.
    """
    pass


class NameRepository(
    NameRepositoryMixin[T], Repository[T, NameCreate, NameUpdate]
):
    """
    Abstract base class for Name object storage repository.
    """
    pass
