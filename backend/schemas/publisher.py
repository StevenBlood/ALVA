from pydantic import BaseModel

class PublisherRead(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
