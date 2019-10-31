# -*- coding: utf-8 -*-
"""
Wedding information SQL-based object repository.
"""
from app.crud.wedding.wedding_info import WeddingInfoRepository
from app.db.crud.base import SQLSingletonRepositoryMixin
from app.db.models.wedding.wedding_info import WeddingInfo


class WeddingInfoSQLRepository(
    SQLSingletonRepositoryMixin,
    WeddingInfoRepository[WeddingInfo]
):
    """
    WeddingInfo SQL-based, singleton object storage repository.
    """
    __obj_cls__ = WeddingInfo
