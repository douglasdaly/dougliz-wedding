# -*- coding: utf-8 -*-
"""
Wedding information SQL-based object repository.
"""
from app.crud.wedding.wedding_info import WeddingInfoRepositoryMixin
from app.db.crud.base import SQLSingletonRepository
from app.db.models.wedding.wedding_info import WeddingInfo
from app.models.wedding.wedding_info import WeddingInfoCreate
from app.models.wedding.wedding_info import WeddingInfoUpdate


class WeddingInfoSQLRepository(
    WeddingInfoRepositoryMixin[WeddingInfo],
    SQLSingletonRepository[WeddingInfo, WeddingInfoCreate, WeddingInfoUpdate]
):
    """
    WeddingInfo SQL-based, singleton object storage repository.
    """
    __obj_cls__ = WeddingInfo
