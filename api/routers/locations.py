from fastapi import APIRouter
from queries.venues import LocationsIn

router = APIRouter()


@router.post("/venues")
def create_location(location: LocationsIn):
    print('venue', location.name)
    return location
