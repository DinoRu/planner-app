from typing import List, Optional
from sqlmodel import JSON, SQLModel, Field, Column
from pydantic import BaseModel


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_typed_allowed = True
        schema_extra = {
            "exemple": {
                "title": "FastApi Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing "
                               "the contents of the FastAPI book inthis event. "
                               "Ensure to come with yourown copy to win gifts!",
                "tags": ["Python", "FastApi", "Book", "Launch"],
                "location": "Google Meet"
            }

        }


class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "exemple": {
                "title": "FastApi Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing "
                               "the contents of the FastAPI book inthis event. "
                               "Ensure to come with yourown copy to win gifts!",
                "tags": ["Python", "FastApi", "Book", "Launch"],
                "location": "Google Meet"
            }
        }

