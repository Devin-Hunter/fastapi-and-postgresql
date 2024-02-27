from pydantic import BaseModel
from typing import Optional


class MembersIn(BaseModel):
    name: str
    from_date: str
    how_long: int
    thoughts: Optional[str]
