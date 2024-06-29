import httpx
import pytest
from auth.jwt_handler import create_access_token
from models.events import Event

#
# @pytest.mark.asyncio
# async def test_get_events(default_client: httpx.AsyncClient, mock_event: Event) -> None:
#     response = await default_client.get("/events/")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)
#     assert response.json()[0]["_id"] == str(mock_event.id)
#

@pytest.mark.asyncio
async def test_get_event(default_client: httpx.AsyncClient, mock_event: Event) -> None:
    url = f"events/{str(mock_event.id)}"
    response = await default_client.get(url)
    assert response.status_code == 200
