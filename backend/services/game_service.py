import requests
from sqlalchemy.orm import Session
from backend.models.game import Game
from backend.config import settings


def fetch_top_games(limit: int = 10) -> list[dict]:
    if not settings.RAWG_API_KEY:
        return []

    url = "https://api.rawg.io/api/games"
    params = {
        "key": settings.RAWG_API_KEY,
        "ordering": "-rating",
        "page_size": limit,
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json().get("results", [])


def save_game(db: Session, game_data: dict) -> Game:
    game = Game(
        name=game_data.get("name"),
        rating=game_data.get("rating"),
        released=game_data.get("released"),
    )
    db.add(game)
    db.commit()
    db.refresh(game)
    return game


def list_games(db: Session) -> list[Game]:
    return db.query(Game).all()
