from pydantic import BaseModel

class UserView(BaseModel):
    id: int
    name: str
    email: str
