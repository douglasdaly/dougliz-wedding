# -*- coding: utf-8 -*-
"""
Wedding database storage repository group.
"""
from app.crud.wedding.core import WeddingRepositoryGroup
from app.db.crud.base import SQLRepositoryGroup
from app.db.crud.wedding.wedding_info import WeddingInfoSQLRepository
from app.utils.proputils import lazy_property


class WeddingSQLRepositoryGroup(WeddingRepositoryGroup, SQLRepositoryGroup):
    """
    Wedding SQL-based repository group.
    """

    @lazy_property
    def wedding_info(self) -> WeddingInfoSQLRepository:
        """WeddingInfoSQLRepository: Wedding information repository."""
        return WeddingInfoSQLRepository(
            self._uow, self._session, *self._args, **self._kwargs
        )
