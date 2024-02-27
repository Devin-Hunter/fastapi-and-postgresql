from fastapi import APIRouter
from queries.venues import VenuesIn

router = APIRouter()

@router.post("/venues")
def create_venue(venue: VenuesIn):
    print('venue', venue.name)
    return venue
