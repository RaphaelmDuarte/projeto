from pydantic import BaseModel
from typing import Optional

class UserForm(BaseModel):
    name: Optional[str] = None
    email: str
    password: str