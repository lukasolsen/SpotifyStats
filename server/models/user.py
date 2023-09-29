from pydantic import BaseModel
from enum import Enum


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserPlan(str, Enum):
    admin = "admin"
    premium = "premium"
    free = "free"


class UserRegister(BaseModel):
    username: str
    email: str
    password: str


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None
    plan: UserPlan


class UserInDB(User):
    hashed_password: str
