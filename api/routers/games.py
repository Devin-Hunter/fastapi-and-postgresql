from fastapi import APIRouter
from queries.games import GameIn

router = APIRouter()

@router.post("/vacatioins")
def create_game(game: GameIn):
    print('game', game.name)
    return game
