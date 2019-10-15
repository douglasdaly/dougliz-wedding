# -*- coding: utf-8 -*-
"""
Wedding information object storage repository.
"""
from abc import ABCMeta
from abc import abstractmethod
import typing as tp

from app.crud.base import SingletonRepository
from app.crud.base import T
from app.models.wedding.wedding_info import WeddingInfoCreate
from app.models.wedding.wedding_info import WeddingInfoUpdate


class WeddingInfoRepositoryMixin(tp.Generic[T], metaclass=ABCMeta):
    """
    WeddingInfo object repository mixin.
    """

    @abstractmethod
    def create(self, obj: WeddingInfoCreate) -> T:
        # - People
        if obj.bride:
            obj.bride = self._uow.person.get_or_create(obj.bride)
        if obj.groom:
            obj.groom = self._uow.person.get_or_create(obj.groom)

        # - Events
        if obj.engagement_party:
            obj.engagement_party = self._uow.event.get_or_create(
                obj.engagement_party
            )
        if obj.welcome:
            obj.welcome = self._uow.event.get_or_create(
                obj.welcome
            )
        if obj.rehearsal_dinner:
            obj.rehearsal_dinner = self._uow.event.get_or_create(
                obj.rehearsal_dinner
            )
        if obj.wedding:
            obj.wedding = self._uow.event.get_or_create(obj.wedding)
        if obj.reception:
            obj.reception = self._uow.event.get_or_create(obj.reception)
        if obj.brunch:
            obj.brunch = self._uow.event.get_or_create(obj.brunch)

        return super().create(obj)

    @abstractmethod
    def update(self, obj: T, updated: WeddingInfoUpdate) -> T:
        # - People
        if updated.bride:
            updated.bride = self._uow.person.get_create_or_update(
                obj.bride, updated.bride
            )
        if updated.groom:
            updated.groom = self._uow.person.get_create_or_update(
                obj.groom, updated.groom
            )

        # - Events
        if updated.engagement_party:
            updated.engagement_party = self._uow.event.get_create_or_update(
                obj.engagement_party, updated.engagement_party
            )
        if updated.welcome:
            updated.welcome = self._uow.event.get_create_or_update(
                obj.welcome, updated.welcome
            )
        if updated.rehearsal_dinner:
            updated.rehearsal_dinner = self._uow.event.get_create_or_update(
                obj.rehearsal_dinner, updated.rehearsal_dinner
            )
        if updated.wedding:
            updated.wedding = self._uow.event.get_create_or_update(
                obj.wedding, updated.wedding
            )
        if obj.reception:
            updated.reception = self._uow.event.get_create_or_update(
                obj.reception, updated.reception
            )
        if updated.brunch:
            updated.brunch = self._uow.event.get_create_or_update(
                obj.brunch, updated.brunch
            )

        return super().update(obj, updated)


class WeddingInfoRepository(
    WeddingInfoRepositoryMixin[T],
    SingletonRepository[T, WeddingInfoCreate, WeddingInfoUpdate]
):
    """
    Abstract base class for WeddingInfo object repository.
    """
    pass
