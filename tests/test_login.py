import httpx
import pytest


@pytest.mark.asyncio(scope="session")
async def test_sign_new_user(default_client: httpx.AsyncClient) -> None:
    payload = {
        "email": "testuser4@packt.com",
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


@pytest.mark.asyncio()
async def test_sign_user_in(default_client: httpx.AsyncClient) -> None:
    payload = {
        "username": "testuser@packt.com",
        "password": "testpassword"
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = await default_client.post(url="/users/signin", data=payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["token_type"] == "Bearer"