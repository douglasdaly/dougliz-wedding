# -*- coding: utf-8 -*-
"""
Core functionality for the actions module.
"""
from abc import ABC
from abc import abstractmethod
import typing as tp

from app.crud.address import AddressRepository
from app.crud.contact_info import ContactInfoRepository
from app.crud.name import NameRepository
from app.crud.person import PersonRepository
from app.crud.user import UserRepository


class UnitOfWork(ABC):
    """
    Abstract base Unit of Work class.
    """

    def __init__(self):
        self._level = 0
        return

    @property
    @abstractmethod
    def address(self) -> AddressRepository:
        """AddressRepository: Address object storage repository."""
        pass

    @property
    @abstractmethod
    def contact_info(self) -> ContactInfoRepository:
        """ContactInfoRepository: ContactInfo object storage repository.
        """
        pass

    @property
    @abstractmethod
    def name(self) -> NameRepository:
        """NameRepository: Name object storage repository."""
        pass

    @property
    @abstractmethod
    def person(self) -> PersonRepository:
        """PersonRepository: Person object storage repository."""
        pass

    @property
    @abstractmethod
    def user(self) -> UserRepository:
        """UserRepository: User object storage repository."""
        pass

    def __enter__(self) -> 'UnitOfWork':
        self._level += 1
        return self

    def __exit__(
        self,
        exc_type: tp.Type[Exception],
        exc_value: Exception,
        traceback
    ) -> None:
        if exc_type is not None:
            self.rollback()
            self._level -= 1
            raise exc_value
        else:
            self.commit()
            self._level -= 1
        return

    @abstractmethod
    def commit(self) -> None:
        """Commits the changes made."""
        pass

    @abstractmethod
    def rollback(self) -> None:
        """Rolls back the changes made."""
        pass
