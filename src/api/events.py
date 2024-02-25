from fastapi import APIRouter
from random import randint
from datetime import datetime
from src.services.events import EventsService
from src.schemas.events import EventSchemaOut, EventSchemaIn, EventSchemaCreateResponse
from typing import Optional
from src.api.dependencies import UOWDep

router = APIRouter(
    prefix="/events",
    tags=["Events"],
)

events = []


@router.get("/events", response_model=list[EventSchemaOut])
async def get_events_handler(uow: UOWDep):
    events = await EventsService().get_events(uow=uow)
    return events


@router.get("/events_today", response_model=list[EventSchemaOut])
async def get_events_today_handler(uow: UOWDep):
    events = await EventsService().get_today_events(uow=uow)
    return events


@router.post("/events", response_model=EventSchemaCreateResponse)
async def create_event_handler(event_data: EventSchemaIn, uow: UOWDep):
    new_event_id: int = await EventsService().add_event(uow=uow, event=event_data)
    return EventSchemaCreateResponse(event_id=new_event_id)
