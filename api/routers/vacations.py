from fastapi import APIRouter
from queries.vacations import VacationIn

router = APIRouter()

@router.post("/vacatioins")
def create_vacation(vacation: VacationIn):
    print('vacation', vacation.name)
    return vacation
