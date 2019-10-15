# -*- coding: utf-8 -*-
"""
Event model.
"""
import datetime
import typing as tp
from uuid import UUID

from app.models.base import AppBaseModel
from app.models.address import Address
from app.models.address import AddressCreate
from app.models.address import AddressUpdate


class EventBase(AppBaseModel):
    """
    Shared attributes for event models.
    """
    name: str
    date: datetime.date
    start: tp.Optional[datetime.time] = None
    end: tp.Optional[datetime.time] = None
    address: tp.Optional[Address] = None


class EventCreate(EventBase):
    """
    Create model for Event objects.
    """
    address: tp.Optional[tp.Union[UUID, AddressCreate]] = None


class EventUpdate(EventBase):
    """
    Update model for Event objects.
    """
    name: tp.Optional[str] = None
    date: tp.Optional[datetime.date] = None
    address: tp.Optional[tp.Union[UUID, AddressCreate, AddressUpdate]] = None


class EventInDBBase(EventBase):
    """
    Storage model base class for Event objects.
    """
    uid: UUID

    class Config:
        orm_mode = True


class Event(EventInDBBase):
    """
    Primary model for Event objects.
    """
    pass


class EventInDB(EventInDBBase):
    """
    Storage model for Event objects.
    """
    id: int
    address_id: int
