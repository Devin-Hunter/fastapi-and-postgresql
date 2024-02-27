from fastapi import APIRouter
from queries.members import MembersIn

router = APIRouter()

@router.post("/members")
def create_members(members: MembersIn):
    print('members', members.name)
    return members
