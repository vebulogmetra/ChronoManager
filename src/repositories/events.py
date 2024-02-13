from src.models.events import Events
from src.utils.repository import SQLAlchemyRepository


class EventsRepository(SQLAlchemyRepository):
    model = Events
