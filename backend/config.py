import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./games.db")
    RAWG_API_KEY: str = os.getenv("RAWG_API_KEY", "")


settings = Settings()
