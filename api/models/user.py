from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.dialects.postgresql import ENUM
from pydantic import BaseModel

from .base import BaseTable


class User(BaseTable):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(ENUM('admin', 'staff', name='user_roles'), default='staff')


class LoginUser(BaseModel):
    username: str
    password: str
