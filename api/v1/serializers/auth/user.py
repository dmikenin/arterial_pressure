from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserRegisterSerializer(BaseModel):
    email: EmailStr = Field(...)
    first_name: str = Field(...)
    password: str = Field(...)
    timezone: int = Field(...)


class UserLoginSerializer(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)