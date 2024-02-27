from pydantic import BaseModel
from typing import Optional


class VacationIn(BaseModel):
    name: str
    from_date: str
    how_long: int
    thoughts: Optional[str]
