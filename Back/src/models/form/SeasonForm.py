from pydantic import BaseModel
from typing import Optional

class SeasonForm(BaseModel):
    id: Optional[int] = None
    season: int
    seriesId: int
    current: bool