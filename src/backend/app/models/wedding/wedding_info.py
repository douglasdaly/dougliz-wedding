# -*- coding: utf-8 -*-
"""
Wedding general information.
"""
import typing as tp
from uuid import UUID

from app.models.base import AppBaseModel
from app.models.base import get_custom_getter
from app.models.event import Event
from app.models.event import EventCreate
from app.models.event import EventUpdate
from app.models.person import Person
from app.models.person import PersonCreate
from app.models.person import PersonUpdate


EventCreateUpdate = tp.Union[UUID, EventCreate, EventUpdate]


class WeddingInfoBase(AppBaseModel):
    """
    Shared attributes for wedding information.
    """
    bride: tp.Optional[Person] = None
    groom: tp.Optional[Person] = None

    engagement_party: tp.Optional[Event] = None
    welcome: tp.Optional[Event] = None
    rehearsal_dinner: tp.Optional[Event] = None
    wedding: tp.Optional[Event] = None
    reception: tp.Optional[Event] = None
    brunch: tp.Optional[Event] = None

    class Config:
        fields = {
            "engagement_party": "engagementParty",
            "rehearsal_dinner": "rehearsalDinner"
        }


class WeddingInfoCreate(WeddingInfoBase):
    """
    Create model for wedding information.
    """
    bride: tp.Optional[tp.Union[UUID, PersonCreate]] = None
    groom: tp.Optional[tp.Union[UUID, PersonCreate]] = None

    engagement_party: tp.Optional[tp.Union[UUID, EventCreate]] = None
    welcome: tp.Optional[tp.Union[UUID, EventCreate]] = None
    rehearsal_dinner: tp.Optional[tp.Union[UUID, EventCreate]] = None
    wedding: tp.Optional[tp.Union[UUID, EventCreate]] = None
    reception: tp.Optional[tp.Union[UUID, EventCreate]] = None
    brunch: tp.Optional[tp.Union[UUID, EventCreate]] = None


class WeddingInfoUpdate(WeddingInfoBase):
    """
    Update model for wedding information.
    """
    bride: tp.Optional[tp.Union[UUID, PersonCreate, PersonUpdate]] = None
    groom: tp.Optional[tp.Union[UUID, PersonCreate, PersonUpdate]] = None

    engagement_party: tp.Optional[EventCreateUpdate] = None
    welcome: tp.Optional[EventCreateUpdate] = None
    rehearsal_dinner: tp.Optional[EventCreateUpdate] = None
    wedding: tp.Optional[EventCreateUpdate] = None
    reception: tp.Optional[EventCreateUpdate] = None
    brunch: tp.Optional[EventCreateUpdate] = None


class WeddingInfoInDBBase(WeddingInfoBase):
    """
    Shared attributes for Event storage model.
    """

    class Config:
        orm_mode = True
        getter_dict = get_custom_getter(WeddingInfoBase)


class WeddingInfo(WeddingInfoInDBBase):
    """
    Primary model for Event objects.
    """
    pass


class WeddingInfoInDB(WeddingInfoInDBBase):
    """
    Storage model for Event objects.
    """
    id: int

    bride_id: tp.Optional[int] = None
    groom_id: tp.Optional[int] = None

    engagement_party_id: tp.Optional[int] = None
    welcome_id: tp.Optional[int] = None
    rehearsal_dinner_id: tp.Optional[int] = None
    wedding_id: tp.Optional[int] = None
    reception_id: tp.Optional[int] = None
    brunch_id: tp.Optional[int] = None
