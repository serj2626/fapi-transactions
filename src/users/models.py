from src.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.transactions import Transaction
    from src.tasks import Task


class User(Base):
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]= mapped_column(Text)


    transactions: Mapped[list["Transaction"]
                         ] = relationship(back_populates="user")
    tasks: Mapped[list["Task"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"<Пользователь {self.username}>"
