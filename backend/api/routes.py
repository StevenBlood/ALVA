from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.services.game_service import (
    fetch_top_games,
    save_game,
    list_games,
)
from backend.schemas.game import GameRead

router = APIRouter(prefix="/games", tags=["Games"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[GameRead])
def get_games(db: Session = Depends(get_db)):
    return list_games(db)


@router.post("/fetch")
def fetch_and_store_games(limit: int = 5, db: Session = Depends(get_db)):
    games = fetch_top_games(limit)
    saved = []
    for g in games:
        saved.append(save_game(db, g))
    return {"saved": len(saved)}
