import threading
import time
import schedule
import logging

from backend.database import SessionLocal
from backend.services.game_service import fetch_top_games, save_game

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def update_games_job():
    logger.info("Automatikus játékfrissítés indul")

    db = SessionLocal()
    try:
        games = fetch_top_games(limit=5)
        for g in games:
            save_game(db, g)
        logger.info("Automatikus frissítés sikeres")
    except Exception as e:
        logger.error(f"Hiba az automatikus frissítés során: {e}")
    finally:
        db.close()


def run_scheduler():
    schedule.every(1).hours.do(update_games_job)

    while True:
        schedule.run_pending()
        time.sleep(60)


def start_scheduler():
    thread = threading.Thread(target=run_scheduler, daemon=True)
    thread.start()
