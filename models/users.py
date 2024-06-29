from typing import Optional, List
from beanie import Document, Link
from pydantic import BaseModel, EmailStr

from models.events import Event


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]]

    class Settings:
        collection = "users"

    class Config:
        json_schema_extra = {
            "exemple": {
                "email": "fastapi@packt.com",
                "password": "Strong!!!!",
                "events": []
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "exemple": {
                "email": "fastapi@packt.com",
                "password": "Strong!!!!",
            }
        }


class TokenResponse(BaseModel):
    access_token: str
    token_type: str