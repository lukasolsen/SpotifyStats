from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum


class UserPlan(str, Enum):
    admin = "admin"
    premium = "premium"
    free = "free"


class UserModel(BaseModel):
    username: str
    email: str
    password: str
    plan: UserPlan
    # Add more user-related fields here


