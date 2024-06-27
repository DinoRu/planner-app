import httpx
import pytest


@pytest.mark.asyncio
async def test_sign_new_user(default_client: httpx.AsyncClient) -> None:
    payload = {
        "email": "testuser1@packt.com",
        "password": "testpassword",
        "events": []
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    test_response = {
        "message": "User was successfully registered!"
    }

    response = await default_client.post(url="/users/signup", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json() == test_response
