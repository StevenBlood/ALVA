from pydantic import BaseModel

class PlatformRead(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
