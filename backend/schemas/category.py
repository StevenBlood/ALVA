from pydantic import BaseModel

class CategoryRead(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
