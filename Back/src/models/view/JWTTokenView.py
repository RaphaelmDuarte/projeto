from pydantic import BaseModel

class JWTTokenView(BaseModel):
    token: str
    userId: int