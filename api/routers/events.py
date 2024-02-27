from fastapi import APIRouter
from queries.events import EventsIn

router = APIRouter()

@router.post("/events")
def create_events(events: EventsIn):
    print('events', events.name)
    return events
