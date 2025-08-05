from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Base User (shared fields)
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: Optional[EmailStr] = None

# Input: User Registration
class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

# Input: User Update
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

# DB Model: What’s stored in MongoDB
class UserInDB(UserBase):
    hashed_password: str

# Output: Public-facing response (no password!)
class UserOut(UserBase):
    id: str  # For MongoDB _id

    class Config:
        from_attributes = True
        populate_by_name = True

class User(UserOut):
    pass
