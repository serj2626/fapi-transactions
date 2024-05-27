from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.orm import mapped_column, Mapped


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr.directive
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"
