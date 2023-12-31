from pydantic import BaseModel
from typing import List, Optional
from models.type.SeasonType import SeasonType

class SeriesForm(BaseModel):
    id: Optional[int] = None
    name: str
    seasons: List[SeasonType]