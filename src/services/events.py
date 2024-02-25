from src.schemas.events import EventSchemaIn, EventSchemaUpdate
from src.utils.unitofwork import IUnitOfWork
from datetime import datetime as dt


class EventsService:
    async def add_event(self, uow: IUnitOfWork, event: EventSchemaIn) -> int:
        event_dict = event.model_dump()
        event_dict.update({"created_at": dt.now()})
        async with uow:
            new_event_id: int = await uow.events.add_one(event_dict)
            await uow.commit()
            return new_event_id

    async def get_events(self, uow: IUnitOfWork):
        async with uow:
            events = await uow.events.find_all()
            return events

    async def get_today_events(self, uow: IUnitOfWork):
        now_date = dt.now().date()
        today_events = []
        async with uow:
            events = await uow.events.find_all()
            for e in events:
                if e.expired_at.date() == now_date:
                    today_events.append(e)
            return today_events

    async def update_event(
        self, uow: IUnitOfWork, event_id: int, event: EventSchemaUpdate
    ):
        events_dict = event.model_dump()
        async with uow:
            await uow.events.update_one(event_id, events_dict)
            await uow.commit()

    async def delete_event(self, event_id: int, uow: IUnitOfWork):
        async with uow:
            events = await uow.events.delete_one(filter_by={"id": event_id})
            return events
