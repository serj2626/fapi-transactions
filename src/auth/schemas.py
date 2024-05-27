from pydantic import BaseModel, EmailStr


class SUserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
