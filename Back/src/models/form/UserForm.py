from typing import Optional
from pydantic import BaseModel

class UserForm(BaseModel):
    name: Optional[str] = None
    email: str
    password: str