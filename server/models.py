from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserModel(BaseModel):
    username: str
    email: str
    password: str
    plan: str
    # Add more user-related fields here


class DataModel(BaseModel):
    user_id: int
    timestamp: str
    total_seconds_played: float
    offline_seconds: float
    online_seconds: float
    total_tracks: int
    total_albums: int
    total_artists: int
    tracks: dict
