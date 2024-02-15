from src.schemas.events import EventSchemaIn, EventSchemaUpdate
from src.utils.unitofwork import IUnitOfWork


class EventsService:
    async def add_event(self, uow: IUnitOfWork, event: EventSchemaIn):
        event_dict = event.model_dump()
        async with uow:
            new_event = await uow.events.add_one(event_dict)
            await uow.commit()
            return new_event

    async def get_events(self, uow: IUnitOfWork):
        async with uow:
            events = await uow.events.find_all()
            return events

    async def update_event(
        self, uow: IUnitOfWork, event_id: int, event: EventSchemaUpdate
    ):
        events_dict = event.model_dump()
        async with uow:
            await uow.events.update_one(event_id, events_dict)
            await uow.commit()
