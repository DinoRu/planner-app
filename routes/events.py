from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event
from typing import List

event_router = APIRouter(tags=["Event"])

events = []


@event_router.get('/', response_model=List[Event])
async def all_events() -> List[Event]:
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="L'Event avec l'id {0} n'existe pas!".format(id)
    )


@event_router.post('/event')
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return {
        "message": "Event created successfully!✨"
    }


@event_router.delete('/{id}')
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {
                "message": "Event delete successfully!"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with applied ID doesn't exists!"
    )


@event_router.delete('/')
async def clear_events():
    events.clear()
    return {
        "message": "List of Events cleared successfully!"
    }
