from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int] = None
    email: str
    first_name: str
    last_name: str
    address: str
    age: int
    joining_date: datetime
    is_registered: bool

