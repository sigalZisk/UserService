from typing import Optional, List

from api.internalApi.poll_system import poll_system_api
from model.user import User
from repository import user_repository


async def create_user(user: User):
    return await user_repository.create_user(user)

async def get_user_by_id(user_id: int) -> Optional[User]:
    return await user_repository.get_by_id(user_id)

async def get_users() -> List[User]:
    return await user_repository.get_users()

async def update_user(user_id: int, user: User):
    await user_repository.update_user(user_id, user)

async def delete_user(user_id: int):
    await poll_system_api.delete_users_answers(user_id)
    await user_repository.delete_user(user_id)

async def register_user(user_id: id):
    await user_repository.register_user(user_id)

async def is_user_registered(user_id: int) -> bool:
    return await user_repository.is_user_registered(user_id)
