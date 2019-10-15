# -*- coding: utf-8 -*-
"""
User repository.
"""
import typing as tp

from app.crud.user import UserRepositoryMixin
from app.db.crud.base import SQLRepository
from app.db.models.user import User
from app.exceptions import ObjectNotFoundError
from app.models.user import UserCreate
from app.models.user import UserUpdate


class UserSQLRepository(
    UserRepositoryMixin[User],
    SQLRepository[User, UserCreate, UserUpdate]
):
    """
    User object storage repository.
    """
    __obj_cls__ = User

    def get_by_email(
        self,
        email: str,
        *,
        raise_ex: bool = False
    ) -> tp.Optional[User]:
        rv = self._session.query(User).filter(User.email == email).first()
        if not rv and raise_ex:
            raise ObjectNotFoundError(User, 'email')
        return rv
