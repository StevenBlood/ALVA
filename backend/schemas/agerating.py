from pydantic import BaseModel

class AgeRatingRead(BaseModel):
    id: int
    value: str

    class Config:
        from_attributes = True
