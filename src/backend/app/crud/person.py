# -*- coding: utf-8 -*-
"""
Person object storage repository.
"""
from abc import abstractmethod
import typing as tp
from uuid import UUID

from app.crud.base import Repository
from app.crud.base import T
from app.models.person import PersonCreate
from app.models.person import PersonUpdate


class PersonRepository(Repository[T, PersonCreate, PersonUpdate]):
    """
    Abstract base Person object storage repository.
    """

    @abstractmethod
    def get_by_name_id(
        self,
        name_id: UUID,
        *,
        raise_ex: bool = False
    ) -> tp.Optional[T]:
        """Gets the person with the associated `name_id` given.

        Parameters
        ----------
        db_session : Session
            The database session to use.
        name_id : UUID
            The associated :obj:`Name` object's ID to get the person
            for.

        Returns
        -------
        :obj:`T` or ``None``
            The person with the matching `name_id` (if found, ``None``
            otherwise).

        """
        pass

    @abstractmethod
    def create(self, obj: PersonCreate) -> T:
        obj.name = self._uow.name.get_or_create(obj.name)
        obj.contact = self._uow.contact_info.get_or_create(obj.contact)
        if obj.address:
            obj.address = self._uow.address.get_or_create(obj.address)
        return super().create(obj)

    @abstractmethod
    def update(self, obj: T, updated: PersonUpdate) -> T:
        if updated.name:
            updated.name = self._uow.address.get_or_update(
                obj.name, updated.name
            )
        if updated.contact:
            updated.contact = self._uow.address.get_or_update(
                obj.contact, updated.contact
            )
        if updated.address:
            updated.address = self._uow.address.get_create_or_update(
                obj.address, updated.address
            )
        return super().update(obj, updated)
