from typing import List, Optional

from starlette import status
from model.user import User
from fastapi import APIRouter, HTTPException

from service import user_service

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: User) -> int:
    try:
        new_user_id = await user_service.create_user(user)
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404, detail="Can't create new user")

    return new_user_id

@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: int) -> Optional[User]:
    existing_user = await user_service.get_user_by_id(user_id)
    if not existing_user:
        raise HTTPException(status_code=400, detail=f"User with id = {user_id} doesn't exist.")
    return existing_user

@router.get("/", response_model=List[User], status_code=status.HTTP_200_OK)
async def get_users() -> List[User]:
    return await user_service.get_users()

@router.put("/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user: User):
    try:
        await user_service.update_user(user_id, user)
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404, detail=f"Can't update user with id {user_id}")

@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int):
    await user_service.delete_user(user_id)

@router.put("/register/{user_id}", status_code=status.HTTP_200_OK)
async def register_user(user_id: int):
    await user_service.register_user(user_id)

@router.get("/registered/{user_id}", status_code=status.HTTP_200_OK)
async def is_user_registered(user_id: int):
    return await user_service.is_user_registered(user_id)
