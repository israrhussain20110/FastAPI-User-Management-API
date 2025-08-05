from bson import ObjectId
from schemas import UserCreate, UserUpdate, UserInDB, UserOut
from auth import get_password_hash
from database import user_collection

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user.get("email"),
    }

async def create_user(user: UserCreate):
    hashed_password = get_password_hash(user.password)
    user_data = user.dict()
    user_data["hashed_password"] = hashed_password
    del user_data["password"]
    result = await user_collection.insert_one(user_data)
    return str(result.inserted_id)

async def get_user(user_id: str):
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return UserOut(**user_helper(user))
    return None

async def get_user_by_username(username: str):
    user = await user_collection.find_one({"username": username})
    if user:
        return UserInDB(**user)
    return None

async def get_all_users(skip: int = 0, limit: int = 100):
    users = await user_collection.find().skip(skip).limit(limit).to_list(length=limit)
    return [UserOut(**user_helper(user)) for user in users]

async def update_user(user_id: str, data: UserUpdate):
    update_data = {k: v for k, v in data.dict().items() if v is not None}
    await user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return UserOut(**user_helper(user))
    return None

async def delete_user(user_id: str):
    return await user_collection.delete_one({"_id": ObjectId(user_id)})