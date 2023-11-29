from pydantic import BaseModel

class Episodes(BaseModel):
    id: int
    number: int
    seasonId: int
    current: bool