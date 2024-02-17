from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from src.schemas.users import UserSchemaOut
from src.storages.database import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=True)
    tg_user_id: Mapped[int] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    def to_schema(self) -> UserSchemaOut:
        return UserSchemaOut(
            id=self.id,
            email=self.email,
            tg_user_id=self.tg_user_id,
            created_at=self.created_at,
        )
