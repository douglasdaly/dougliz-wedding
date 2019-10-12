# -*- coding: utf-8 -*-
"""
Base class for CRUD repositories.
"""
from abc import ABCMeta
from abc import abstractmethod
import typing as tp
from uuid import UUID

if tp.TYPE_CHECKING:
    from app.crud.core import UnitOfWork


T = tp.TypeVar('T')
C = tp.TypeVar('C')
U = tp.TypeVar('U')


class Repository(tp.Generic[T, C, U], metaclass=ABCMeta):
    """
    Abstract base class for object storage repositories.

    Parameters
    ----------
    unit_of_work : UnitOfWork
        The current unit of work object to use.

    """
    __obj_cls__: tp.Type[T]

    def __init__(self, unit_of_work: 'UnitOfWork') -> None:
        self._uow = unit_of_work
        return

    @abstractmethod
    def get(
        self,
        id: UUID,
        *,
        raise_ex: bool = False
    ) -> tp.Optional[T]:
        """Gets the object with the specified UUID.

        Parameters
        ----------
        id : UUID
            The UUID identifer of the object to get (corresponding to
            the object's ``uid`` field).
        raise_ex : bool, optional
            Whether or not to raise an exception if the object isn't
            found (default is ``False``).

        Returns
        -------
        :obj:`T` or ``None``
            The object with the `id` given (if found, ``None``
            otherwise).

        Raises
        ------
        ObjectNotFoundException
            If the object with the given `id` wasn't found and the
            `raise_ex` parameter is set to ``True``.

        """
        pass

    @abstractmethod
    def get_by_id(
        self,
        id: int,
        *,
        raise_ex: bool = False
    ) -> tp.Optional[T]:
        """Gets the object with the specified `id`.

        Parameters
        ----------
        db_session : Session
            The database session to use.
        id : UUID
            The UUID identifer of the object to get (corresponding to
            the object's ``id`` field).
        raise_ex : bool, optional
            The object with the `id` given (if found, ``None``
            otherwise).

        Returns
        -------
        :obj:`T` or ``None``
            The object with the `id` given (if found, ``None``
            otherwise).

        Raises
        ------
        ObjectNotFoundException
            If the object with the given `id` wasn't found and the
            `raise_ex` parameter is set to ``True``.

        """
        pass

    @abstractmethod
    def all(
        self,
        *,
        skip: tp.Optional[int] = None,
        limit: tp.Optional[int] = None
    ) -> tp.List[T]:
        """Gets all objects in the repository.

        Parameters
        ----------
        skip : int, optional
            The number of items to skip when fetching all.
        limit : int, optional
            The number of items to limit results to when fetching all.

        Returns
        -------
        List[T]
            The list of objects requested.

        """
        pass

    def create(self, obj: C) -> T:
        """Creates and stores a new object.

        Parameters
        ----------
        obj : C
            The data for the new object to create.

        Returns
        -------
        T
            The newly created object.

        """
        return self.__obj_cls__(**dict(obj))

    def get_or_create(
        self,
        new_obj: tp.Union[UUID, C]
    ) -> T:
        """Gets or creates the specified object.

        Parameters
        ----------
        new_obj : Union[UUID, C]
            The object ID or object creation data to use.

        Returns
        -------
        :obj:`T` or ``None``
            The fetched/created object specified.

        """
        if isinstance(new_obj, UUID):
            return self.get(new_obj, raise_ex=True)
        else:
            return self.create(new_obj)

    def update(self, obj: T, updated: U) -> T:
        """Updates an existing object with new data.

        Parameters
        ----------
        obj : T
            The current object to update.
        updated : U
            The data to update `obj` with.

        Returns
        -------
        T
            The updated object.

        """
        update_fields = updated.dict(skip_defaults=True).keys()
        for field, value in updated:
            if field not in update_fields:
                continue
            setattr(obj, field, value)
        return obj

    def get_or_update(
        self,
        obj: T,
        updated: tp.Optional[tp.Union[UUID, U]]
    ) -> T:
        """Gets or updates the specified object.

        Parameters
        ----------
        obj : T
            The object to update.
        updated : Union[UUID, C]
            The object ID or object update data to use.

        Returns
        -------
        :obj:`T` or ``None``
            The fetched/updated object specified.

        """
        if isinstance(updated, UUID):
            return self.get(updated, raise_ex=True)
        else:
            return self.update(obj, updated)

    def get_create_or_update(
        self,
        obj: tp.Optional[T],
        new_data: tp.Union[UUID, C, U]
    ) -> T:
        """Gets, updates or creates the specified object.

        Parameters
        ----------
        obj : Optional[T]
            The current object (if any).
        new_data : Union[UUID, C, U]
            The new data to use to either create or update.

        Returns
        -------
        T
            The newly created/updated object.

        """
        if isinstance(new_data, UUID):
            return self.get(new_data, raise_ex=True)
        if obj:
            return self.update(obj, new_data)
        else:
            return self.create(new_data)

    @abstractmethod
    def delete(self, obj: T) -> T:
        """Deletes an object from this repository.

        Parameters
        ----------
        obj : T
            The object to remove.

        Returns
        -------
        T
            The removed object.

        """
        pass
