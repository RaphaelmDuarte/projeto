from pydantic import BaseModel

class Season(BaseModel):
    id: int
    value: int
    seriesId: int
    current: bool | None = False