from typing import List, Optional
from beanie import Document
from pydantic import BaseModel


class Event(Document):
    creator: Optional[str]
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
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

    class Settings:
        collection = "events"


class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        json_schema_extra = {
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

