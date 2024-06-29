import asyncio

import httpx
import pytest

from auth.jwt_handler import create_access_token
from database.connections import Settings
from main import app
from models.events import Event
from models.users import User


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


async def init_db():
    test_settings = Settings()
    test_settings.DATABASE_URL = "mongodb://localhost:27017/testdb"

    await test_settings.initialize_database()


@pytest.fixture(scope="session")
async def default_client():
    await init_db()
    async with httpx.AsyncClient(app=app, base_url="http://app") as client:
        yield client

        # Clean up resources
        # await Event.find_all().delete()
        # await User.find_all().delete()


@pytest.fixture(scope='module')
async def access_token() -> str:
    return create_access_token("testuser@packt.com")


@pytest.fixture(scope="module")
async def mock_event() -> Event:
    new_event = Event(
        creator="testuser@packt.com",
        title="FastAPI Book Launch",
        image="https://linktomyimage.com/image.png",
        description="We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
        tags=["python", "fastapi", "book", "launch"],
        location="Google Meet"
    )
    await Event.insert_one(new_event)
    yield new_event
    yield new_event
    await new_event.delete()
