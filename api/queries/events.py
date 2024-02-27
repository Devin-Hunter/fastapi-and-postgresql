from pydantic import BaseModel
from typing import Optional


class EventsIn(BaseModel):
    name: str
    from_date: str
    how_long: int
    thoughts: Optional[str]
