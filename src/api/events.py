from fastapi import APIRouter
from random import randint
from datetime import datetime
from src.schemas.events import EventSchemaOut, EventSchemaIn

router = APIRouter(
    prefix="/events",
    tags=["Events"],
)

events = []


@router.get("/events", response_model=list[EventSchemaOut])
async def get_events_handler():
    return events


@router.post("/events", response_model=list[EventSchemaOut])
async def create_event_handler(event_data: EventSchemaIn):
    events.append(
        EventSchemaOut(
            id=randint(1, 10),
            title=event_data.title,
            description=event_data.description,
            expired_at=event_data.expired_at,
            created_at=datetime.now(),
        )
    )
    return events
