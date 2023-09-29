from pydantic import BaseModel


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
