from typing import Optional, List

from model.user import User
from repository.database import database

TABLE_NAME = "users"

async def create_user(user: User):
    query = f"""
        INSERT INTO {TABLE_NAME} (email, first_name, last_name, address, age)
        VALUES (:email, :first_name, :last_name, :address, :age)
    """
    values = {"email": user.email,
              "first_name": user.first_name,
              "last_name": user.last_name,
              "address": user.address,
              "age": user.age
              }

    async with database.transaction():
        await database.execute(query, values=values)
        last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")

    return last_record_id[0]

async def get_by_id(user_id: int) -> Optional[User]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id=:user_id"
    result = await database.fetch_one(query, values={"user_id": user_id})
    if result:
        return User(**result)
    else:
        return None

async def get_users() -> List[User]:
    query = f"SELECT * FROM {TABLE_NAME}"
    results = await database.fetch_all(query)
    return [User(**result) for result in results]

async def update_user(user_id: int, user: User):
    query = f"""
            UPDATE {TABLE_NAME} 
            SET email = :email, 
                first_name = :first_name, 
                last_name = :last_name,
                address = :address, 
                age = :age
            WHERE id = :user_id
        """

    values = {"user_id": user_id,
              "email": user.email,
              "first_name": user.first_name,
              "last_name": user.last_name,
              "address": user.address,
              "age": user.age
              }

    await database.execute(query, values)

async def delete_user(user_id: int):
    query = f"DELETE FROM {TABLE_NAME} WHERE id = :user_id"

    await database.execute(query, values={"user_id": user_id})

async def register_user(user_id: int):
    query = f"""
            UPDATE {TABLE_NAME} 
            SET is_registered = true
            WHERE id = :user_id
        """

    await database.execute(query, values={"user_id": user_id})

async def is_user_registered(user_id: int) -> bool:
    query = f"""SELECT is_registered 
                FROM {TABLE_NAME}
                WHERE id = :user_id
            """

    return await database.fetch_one(query, values={"user_id": user_id})
