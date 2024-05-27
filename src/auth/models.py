from src.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.transactions import Transaction
    from src.tasks import Task


class User(Base):
    username: Mapped[str] = mapped_column(String(26), unique=True)
    email: Mapped[str] = mapped_column(String(36), unique=True)
    password: Mapped[str] = mapped_column(nullable=False)

    transactions: Mapped[list["Transaction"]] = relationship(back_populates="user")
    tasks: Mapped[list["Task"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"<Пользователь {self.username}>"
