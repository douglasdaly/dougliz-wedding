# -*- coding: utf-8 -*-
"""
User repository.
"""
import typing as tp

from app.crud.user import UserRepository
from app.db.crud.base import SQLRepositoryMixin
from app.db.models.user import User
from app.exceptions import ObjectNotFoundError


class UserSQLRepository(SQLRepositoryMixin, UserRepository[User]):
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
