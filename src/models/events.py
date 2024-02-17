from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from src.schemas.events import EventSchemaOut
from src.storages.database import Base


class Events(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    created_at: Mapped[datetime]
    expired_at: Mapped[datetime]
    notify_at: Mapped[datetime]
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    def to_schema(self) -> EventSchemaOut:
        return EventSchemaOut(
            id=self.id,
            title=self.title,
            description=self.description,
            owner_id=self.owner_id,
            expired_at=self.expired_at,
            notify_at=self.notify_at,
            created_at=self.created_at,
        )
