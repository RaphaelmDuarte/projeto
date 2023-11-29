from pydantic import BaseModel

class Series(BaseModel):
    id: int
    name: str