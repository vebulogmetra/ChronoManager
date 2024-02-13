from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from src.storages.database import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    created_at: Mapped[datetime]
