from src.database import async_session
from src.auth.models import User
from sqlalchemy import select
from .schemas import SUserCreate


class AuthCRUD:
    _model = None

    @classmethod
    async def get_user_by_id(cls, user_id: int) -> User:
        async with async_session() as session:
            query = select(cls._model).filter_by(id=user_id)
            result = await session.execute(query)
            return result.scalar()

    @classmethod
    async def create_user(cls, user: SUserCreate) -> User:
        async with async_session() as session:
            new_user = User(**user.model_dump())
            session.add(new_user)
            await session.commit()
            return new_user
