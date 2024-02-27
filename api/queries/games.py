from pydantic import BaseModel
from typing import Optional


class GamesIn(BaseModel):
    name: str
    from_date: str
    how_long: int
    thoughts: Optional[str]
