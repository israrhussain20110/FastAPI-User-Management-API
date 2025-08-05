from fastapi import APIRouter, Depends, HTTPException, status
from schemas import User, UserCreate, UserOut, UserUpdate
import crud
from auth import get_current_active_user

router = APIRouter()

async def get_user_or_404(user_id: str):
    user = await crud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    db_user = await crud.get_user_by_username(user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    user_id = await crud.create_user(user)
    new_user = await get_user_or_404(user_id)
    return new_user

@router.get("/", response_model=list[User])
async def read_users(skip: int = 0, limit: int = 100, current_user: dict = Depends(get_current_active_user)):
    return await crud.get_all_users(skip=skip, limit=limit)

@router.get("/{user_id}", response_model=User)
async def read_user(user_id: str, current_user: dict = Depends(get_current_active_user)):
    return await get_user_or_404(user_id)

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: str, user: UserUpdate, current_user: dict = Depends(get_current_active_user)):
    if current_user["_id"] != user_id and current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to update this user")
    updated_user = await crud.update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}")
async def delete_user(user_id: str, current_user: dict = Depends(get_current_active_user)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admins can delete users")
    result = await crud.delete_user(user_id)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}