from typing import Optional, List
from pydantic import BaseModel, EmailStr

from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "exemple": {
                "email": "fastapi@packt.com",
                "password": "Strong!!!!",
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "exemple": {
                "email": "fastapi@packt.com",
                "password": "Strong!!!!",
            }
        }