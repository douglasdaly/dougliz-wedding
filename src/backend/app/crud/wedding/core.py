# -*- coding: utf-8 -*-
"""
Wedding model object storage repository group.
"""
from abc import ABCMeta
from abc import abstractmethod

from app.crud.base import RepositoryGroup
from app.crud.wedding.wedding_info import WeddingInfoRepository


class WeddingRepositoryGroup(RepositoryGroup, metaclass=ABCMeta):
    """
    Wedding storage repository grouper.
    """

    @property
    @abstractmethod
    def wedding_info(self) -> WeddingInfoRepository:
        """WeddingInfoRepository: Wedding information storage
        repository."""
        pass
