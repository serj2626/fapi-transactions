from src.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from src.service.mixins import UserRelationshipMixin


class Task(UserRelationshipMixin, Base):
    _user_back_populates = "tasks"

    title: Mapped[str]
    is_completed: Mapped[bool] = mapped_column(
        default=False, server_default="false")

    def __repr__(self):
        return f"<Task {self.title}>"
