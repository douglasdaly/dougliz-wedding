# -*- coding: utf-8 -*-
"""
Event object database storage repository.
"""
import datetime
import typing as tp
from uuid import UUID

from app.crud.event import EventRepository
from app.crud.event import EventRepositoryMixin
from app.db.crud.base import SQLRepository
from app.db.models.address import Address
from app.db.models.event import Event
from app.exceptions import ObjectNotFoundError
from app.models.event import EventCreate
from app.models.event import EventUpdate


class EventSQLRepository(
    EventRepositoryMixin[Event],
    SQLRepository[Event, EventCreate, EventUpdate]
):
    """
    Event object database storage repository.
    """
    __obj_cls__ = Event

    def get_by_address_id(
        self,
        address_id: UUID,
        *,
        raise_ex: bool = False
    ) -> tp.List[Address]:
        rv = self._session.query(Event).join(Address) \
            .filter(Address.uid == address_id) \
            .all()
        if not rv and raise_ex:
            raise ObjectNotFoundError(Event, 'address_id')
        return rv

    def get_by_date(
        self,
        date: datetime.date,
        *,
        raise_ex: bool = False
    ) -> tp.List[Event]:
        rv = self._session.query(Event) \
            .filter(Event.date == date) \
            .all()
        if not rv and raise_ex:
            raise ObjectNotFoundError(Event, 'date')
        return rv


# Register as subclass
EventRepository.register(EventSQLRepository)
