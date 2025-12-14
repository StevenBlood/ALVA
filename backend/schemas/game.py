from backend.schemas.category import CategoryRead
from backend.schemas.agerating import AgeRatingRead
from backend.schemas.platform import PlatformRead
from backend.schemas.publisher import PublisherRead
from backend.schemas.developer import DeveloperRead
from pydantic import BaseModel


class GameBase(BaseModel):
    name: str
    rating: float | None = None
    released: str | None = None


class GameCreate(GameBase):
    pass


class GameRead(BaseModel):
    id: int
    name: str
    released: str

    platform: PlatformRead
    publisher: PublisherRead | None = None
    developer: DeveloperRead | None = None

    category1: CategoryRead
    category2: CategoryRead | None
    agerating: AgeRatingRead | None

    class Config:
        from_attributes = True