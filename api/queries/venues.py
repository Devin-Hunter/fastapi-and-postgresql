from pydantic import BaseModel
from typing import Optional


class VenuesIn(BaseModel):
    name: str
    from_date: str
    how_long: int
    thoughts: Optional[str]

class LocationsIn(BaseModel):
    name: str
    from_date: str
    how_long: int
    thoughts: Optional[str]
