from enum import Enum
from src.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import text
from datetime import datetime
from src.service.mixins import UserRelationshipMixin


class TypeOperation(str, Enum):
    INCOME = "Доходы"
    EXPENSE = "Расходы"


class Category(str, Enum):
    SALARY = "Зарплата"
    FOOD = "Еда"
    TRANSPORTATION = "Транспорт"
    HOUSEHOLD = "Хозяйственные нужды"
    ENTERTAINMENT = "Развлечения"
    HEALTH = "Здоровье"
    EDUCATION = "Образование"
    TRAVEL = "Путешествия"
    OTHER = "Другое"


class Transaction(UserRelationshipMixin, Base):
    _user_back_populates = "transactions"

    type: Mapped[TypeOperation]
    category: Mapped[Category]
    description: Mapped[str | None]
    price: Mapped[int] = mapped_column(default=0, server_default="0")
    date: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

    def __repr__(self) -> str:
        return f"Транзакция {self.type} на сумму {self.price}"
