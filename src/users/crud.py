from src.database import async_session
from .models import User
from sqlalchemy import insert, select
from src.service import BaseCRUD


class UserCRUD(BaseCRUD):
    model = User
