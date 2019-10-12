# -*- coding: utf-8 -*-
"""
User repository.
"""
from abc import abstractmethod
import typing as tp

from app.core.security import get_password_hash
from app.core.security import verify_password
from app.crud.base import Repository
from app.crud.base import T
from app.models.user import UserCreate
from app.models.user import UserUpdate


class UserRepository(Repository[T, UserCreate, UserUpdate]):
    """
    User object storage repository.
    """

    @abstractmethod
    def get_by_email(
        self,
        email: str,
        *,
        raise_ex: bool = False
    ) -> tp.Optional[T]:
        """Gets the user with the associated `email` given.

        Parameters
        ----------
        email : str
            The user's email to get the associated User object for.
        raise_ex : bool, optional
            Whether or not to raise an exception if the object for the
            given `email` wasn't found (default is ``False``).

        Returns
        -------
        :obj:`T` or ``None``
            The user with the matching `email` (if found, ``None``
            otherwise).

        """
        pass

    @abstractmethod
    def create(self, obj: UserCreate) -> T:
        """Creates a new User object.

        Parameters
        ----------
        obj : UserCreate
            The new user data object.

        Returns
        -------
        T
            The newly created user object.

        """
        if obj.person:
            obj.person = self._uow.person.get_or_create(obj.person)
        data = dict(obj)
        hashed_password = get_password_hash(data.pop('password'))
        return self.__obj_cls__(**data, hashed_password=hashed_password)

    @abstractmethod
    def update(self, obj: T, updated: UserUpdate) -> T:
        if updated.person:
            updated.person = self._uow.person.get_create_or_update(
                obj.person, updated.person
            )
        if updated.password:
            obj.hashed_password = get_password_hash(updated.password)
            updated.password = None
        return super().update(obj, updated)

    def authenticate(self, email: str, password: str) -> tp.Optional[T]:
        """Authenticates (and returns) the user with given credentials.

        Parameters
        ----------
        email : str
            The user's email address.
        password : str
            The plaintext password to validate.

        Returns
        -------
        T
            The authenticated User object (if verified, ``None``
            otherwise).

        """
        user = self.get_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
