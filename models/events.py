from typing import List

from pydantic import BaseModel


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

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

