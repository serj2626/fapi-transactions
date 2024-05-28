from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.config import settings


engine = create_async_engine(url=settings.DATABASE_URL, echo=settings.DB_ECHO)
async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
