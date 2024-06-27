from fastapi import APIRouter, Body, HTTPException, status, Depends
from beanie import PydanticObjectId
from models.events import Event, EventUpdate
from database.connections import Database
from typing import List
from auth.authenticate import authenticate

event_router = APIRouter(tags=["Event"])
event_database = Database(Event)


@event_router.get('/', response_model=List[Event])
async def all_events() -> List[Event]:
    events = await event_database.get_all()
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="L'Event avec l'id {0} n'existe pas!".format(id)
        )
    return event


@event_router.post('/event')
async def create_event(body: Event, user: str = Depends(authenticate)) -> dict:
    body.creator = user
    await event_database.save(body)
    return {
        "message": "Event created successfully!✨"
    }


@event_router.put('/edit/{id}', response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate, user: str = Depends(authenticate)) -> Event:
    event = await event_database.get(id)
    if event.creator != user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Operation not allowed"
        )
    updated_event = await event_database.update(id, body)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with applied ID doesn't exists!"
        )
    return updated_event


@event_router.delete('/{id}')
async def delete_event(id: PydanticObjectId, user: str = Depends(authenticate)) -> dict:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with applied ID doesn't exists!"
        )
    if event.creator != user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    event = await event_database.delete(id)
    return {
        "message": "Event deleted successfully!"
    }

#
# @event_router.delete('/')
# async def clear_events():
#     events.clear()
#     return {
#         "message": "List of Events cleared successfully!"
#     }
