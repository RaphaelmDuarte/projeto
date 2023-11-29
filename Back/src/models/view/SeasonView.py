from pydantic import BaseModel

class SeasonView(BaseModel):
    id: int
    season: int
    seriesId: int
    current: bool