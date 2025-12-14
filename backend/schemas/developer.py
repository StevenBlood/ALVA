from pydantic import BaseModel

class DeveloperRead(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
