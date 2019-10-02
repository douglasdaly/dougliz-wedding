# -*- coding: utf-8 -*-
"""
User model.
"""
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    """
    Shared properties of User model objects.
    """
    name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False


class UserBaseInDB(UserBase):
    """
    Database representation of User model.
    """
    id: Optional[int] = None

    class Config:
        orm_mode = True


class UserCreate(UserBaseInDB):
    """
    Object used for creating new User objects.
    """
    email: str
    password: str


class UserUpdate(UserBaseInDB):
    """
    Object used for updating User objects.
    """
    password: Optional[str] = None


class User(UserBaseInDB):
    """
    Primary User model object.
    """
    pass


class UserInDB(UserBaseInDB):
    """
    Primary database User model object.
    """
    hashed_password: str
