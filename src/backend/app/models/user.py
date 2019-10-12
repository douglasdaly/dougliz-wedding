# -*- coding: utf-8 -*-
"""
User model.
"""
import typing as tp
from uuid import UUID

from pydantic import BaseModel
from pydantic import EmailStr

from app.models.person import Person
from app.models.person import PersonCreate
from app.models.person import PersonUpdate


class UserBase(BaseModel):
    """
    Shared properties of User model objects.
    """
    person: tp.Optional[Person] = None
    email: EmailStr
    is_active: bool = True
    is_poweruser: bool = False
    is_superuser: bool = False


class UserCreate(UserBase):
    """
    Object used for creating new User objects.
    """
    person: tp.Optional[tp.Union[UUID, PersonCreate]] = None
    password: str


class UserUpdate(UserBase):
    """
    Object used for updating User objects.
    """
    email: tp.Optional[EmailStr] = None
    password: tp.Optional[str] = None
    person: tp.Optional[tp.Union[UUID, PersonCreate, PersonUpdate]] = None
    is_active: tp.Optional[bool] = None
    is_poweruser: tp.Optional[bool] = None
    is_superuser: tp.Optional[bool] = None


class UserBaseInDB(UserBase):
    """
    Database representation of User model.
    """
    uid: tp.Optional[UUID] = None

    class Config:
        orm_mode = True


class User(UserBaseInDB):
    """
    Primary User model object.
    """
    pass


class UserInDB(UserBaseInDB):
    """
    Primary database User model object.
    """
    id: int
    person_id: tp.Optional[int]
    hashed_password: str
