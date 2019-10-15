# -*- coding: utf-8 -*-
"""
Event repository.
"""
from abc import abstractmethod
import datetime
import typing as tp
from uuid import UUID

from app.crud.base import Repository
from app.crud.base import T
from app.models.event import EventCreate
from app.models.event import EventUpdate


class EventRepositoryMixin(tp.Generic[T]):
    """
    Event object repository mixin.
    """

    @abstractmethod
    def get_by_address_id(
        self,
        address_id: UUID,
        *,
        raise_ex: bool = False
    ) -> tp.List[T]:
        """Gets the event(s) associated with the `address_id` given.

        Parameters
        ----------
        address_id : UUID
            The associated :obj:`Address` object's ID to get the
            event(s) for.
        raise_ex : bool, optional
            Whether or not to raise an exception if none are found
            (default is ``False``).

        Returns
        -------
        List[T]
            The event(s) associated with the `address_id` location
            given (if any).

        """
        pass

    @abstractmethod
    def get_by_date(
        self,
        date: datetime.date,
        *,
        raise_ex: bool = False
    ) -> tp.List[T]:
        """Gets the event(s) associated with the `date` given.

        Parameters
        ----------
        date : datetime.date
            The date to get the event(s) for.
        raise_ex : bool, optional
            Whether or not to raise an exception if none are found
            (default is ``False``).

        Returns
        -------
        List[T]
            The event(s) associated with the `date` given (if any).

        """
        pass

    @abstractmethod
    def create(self, obj: EventCreate) -> T:
        if obj.address:
            obj.address = self._uow.address.get_or_create(obj.address)
        return super().create(obj)

    @abstractmethod
    def update(self, obj: T, updated: EventUpdate) -> T:
        if updated.address:
            updated.address = self._uow.address.get_create_or_update(
                obj.address, updated.address
            )
        return super().update(obj, updated)


class EventRepository(
    EventRepositoryMixin[T], Repository[T, EventCreate, EventUpdate]
):
    """
    Abstract base class for Event object repositories.
    """
    pass
