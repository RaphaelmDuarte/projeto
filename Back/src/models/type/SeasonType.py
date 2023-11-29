from pydantic import BaseModel

class SeasonType(BaseModel):
    season: int
    episodes: int