# -*- coding: utf-8 -*-
"""
Events API endpoints.
"""
import datetime
import typing as tp
from uuid import UUID

from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import Query

from app.api.utils.security import get_current_active_poweruser
from app.api.utils.security import get_current_active_user
from app.api.utils.storage import get_uow
from app.crud.core import UnitOfWork
from app.db.models.event import Event as DBEvent
from app.models.event import Event
from app.models.event import EventCreate
from app.models.event import EventUpdate
from app.models.user import UserInDB


router = APIRouter()


@router.post("/", response_model=Event)
async def create_event(
    *,
    new_event: EventCreate = Body(...),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> DBEvent:
    """Creates a new Event object.

    Parameters
    ----------
    new_event : EventCreate
        The new event data to create a new Event object with.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current poweruser making the call.

    Returns
    -------
    DBEvent
        The newly created Event object.

    Raises
    ------
    ObjectExistsException
        If this event already exists.

    """
    with uow:
        return uow.event.create(new_event)


@router.get("/", response_model=tp.List[Event])
async def read_upcoming_events(
    *,
    skip: tp.Optional[int] = Query(None),
    limit: tp.Optional[int] = Query(None),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_user)
) -> tp.List[DBEvent]:
    """Gets all the event objects.

    Parameters
    ----------
    skip : int, optional
        The number of events to skip in the results.
    limit : int, optional
        The number of events to limit the result to.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current user making the request.

    Returns
    -------
    List[DBEvent]
        The Event object(s) requested.

    """
    return uow.event.all_in_range(start_date=datetime.date.today(), skip=skip,
                                  limit=limit)


@router.get("/all", response_model=tp.List[Event])
async def read_all_events(
    *,
    skip: tp.Optional[int] = Query(None),
    limit: tp.Optional[int] = Query(None),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> tp.List[DBEvent]:
    """Gets all the event objects.

    Parameters
    ----------
    skip : int, optional
        The number of events to skip in the results.
    limit : int, optional
        The number of events to limit the result to.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current power user making the request.

    Returns
    -------
    List[DBEvent]
        The Event object(s) requested.

    """
    return uow.event.all(skip=skip, limit=limit)


@router.get("/id/{event_id}", response_model=Event)
async def read_event(
    event_id: UUID,
    *,
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> DBEvent:
    """Gets the event with the specified `event_id`.

    Parameters
    ----------
    event_id : UUID
        The event ID to get the associated event for.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current power user making the request.

    Returns
    -------
    DBEvent
        The Event object requested.

    Raises
    ------
    ObjectNotFoundError
        If the object with the specified `event_id` doesn't exist.

    """
    return uow.event.get(event_id, raise_ex=True)


@router.put("/id/{event_id}", response_model=Event)
async def update_event(
    event_id: UUID,
    *,
    updated_event: EventUpdate = Body(...),
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> DBEvent:
    """Updates the event with the specified `event_id`.

    Parameters
    ----------
    event_id : UUID
        The event ID to update.
    updated_event : EventUpdate
        The data to update the event with.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current power user making the request.

    Returns
    -------
    DBEvent
        The updated Event object.

    Raises
    ------
    ObjectNotFoundError
        If the object with the specified `event_id` doesn't exist.

    """
    current = uow.event.get(event_id, raise_ex=True)
    with uow:
        return uow.event.update(current, updated_event)


@router.delete("/id/{event_id}", response_model=Event)
async def delete_event(
    event_id: UUID,
    *,
    uow: UnitOfWork = Depends(get_uow),
    current_user: UserInDB = Depends(get_current_active_poweruser)
) -> DBEvent:
    """Deletes the event with the specified `event_id`.

    Parameters
    ----------
    event_id : UUID
        The event ID for the event to delete.
    uow : UnitOfWork
        The unit of work to use.
    current_user : UserInDB
        The current power user making the request.

    Returns
    -------
    DBEvent
        The deleted Event object.

    Raises
    ------
    ObjectNotFoundError
        If the object with the specified `event_id` doesn't exist.

    """
    current = uow.event.get(event_id, raise_ex=True)
    with uow:
        return uow.event.delete(current)
