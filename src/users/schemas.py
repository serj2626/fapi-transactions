from pydantic import BaseModel, EmailStr, Field


class SUserAuth(BaseModel):
    username: str
    email: str
    password: str
