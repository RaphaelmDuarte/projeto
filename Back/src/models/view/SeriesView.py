from pydantic import BaseModel

class SeriesView(BaseModel):
    id: int
    name: str