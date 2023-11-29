from pydantic import BaseModel
from typing import Optional

class EpisodesForm(BaseModel):
    id: Optional[int] = None
    episode: int
    name: str
    seasonId: int
    current: bool