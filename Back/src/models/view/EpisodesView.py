from pydantic import BaseModel

class EpisodesView(BaseModel):
    id: int
    episode: int
    name: str
    seasonId: int
    current: bool