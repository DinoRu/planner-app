from fastapi import APIRouter, HTTPException, status, Depends
from beanie import PydanticObjectId
from fastapi.security import OAuth2PasswordRequestForm
from auth.jwt_handler import create_access_token
from auth.hash_password import HashPassword
from database.connections import Database

from models.users import User, TokenResponse

user_route = APIRouter(
    tags=["User"]
)
user_database = Database(User)
hash_password = HashPassword()


@user_route.post("/signup")
async def sign_new_user(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists."
        )
    hashed_password = hash_password.create_hash(user.password)
    user.password = hashed_password
    await user_database.save(user)
    return {
        "message": "User was successfully registered!"
    }


@user_route.post("/signin", response_model=TokenResponse)
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends()) -> dict:
    user_exit = await User.find_one(User.email == user.username)
    if not user_exit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with this email doesn't exists!"
        )

    if hash_password.verify_hash(user.password, user_exit.password):
        access_token = create_access_token(user_exit.email)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid details passed"
    )