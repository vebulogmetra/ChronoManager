from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from src.storages.database import Base


class Events(Base):
    __tablename__ = "user_events"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    descroption: Mapped[str]
    expired_at: Mapped[datetime]
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
