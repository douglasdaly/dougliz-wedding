# -*- coding: utf-8 -*-
"""
Base class for CRUD repositories.
"""
from abc import ABCMeta
import typing as tp
from uuid import UUID

from sqlalchemy.orm import Session

from app.crud.base import Repository
from app.crud.base import (T, C, U)
from app.exceptions import ObjectNotFoundError

if tp.TYPE_CHECKING:
    from app.crud.core import UnitOfWork


class SQLRepository(Repository[T, C, U], metaclass=ABCMeta):
    """
    SQLAlchemy-based object storage repository base class.

    Parameters
    ----------
    unit_of_work : UnitOfWork
        The unit of work object to use.
    db_session : Session
        The SQL Alchemy session object to use.

    """

    def __init__(
        self,
        unit_of_work: 'UnitOfWork',
        db_session: Session
    ) -> None:
        self._session = db_session
        return super().__init__(unit_of_work)

    def get(
        self,
        id: UUID,
        *,
        raise_ex: bool = False
    ) -> tp.Optional[T]:
        rv = self._session.query(self.__obj_cls__) \
            .filter(self.__obj_cls__.uid == id) \
            .first()
        if not rv and raise_ex:
            raise ObjectNotFoundError(self.__obj_cls__, 'id')
        return rv

    def get_by_id(
        self,
        id: int,
        *,
        raise_ex: bool = False
    ) -> tp.Optional[T]:
        rv = self._session.query(self.__obj_cls__) \
            .filter(self.__obj_cls__.id == id) \
            .first()
        if not rv and raise_ex:
            raise ObjectNotFoundError(self.__obj_cls__, 'id')
        return rv

    def all(
        self,
        *,
        skip: tp.Optional[int] = None,
        limit: tp.Optional[int] = None
    ) -> tp.List[T]:
        return self._session.query(self.__obj_cls__) \
            .offset(skip) \
            .limit(limit) \
            .all()

    def create(self, obj: C) -> T:
        new_obj = super().create(obj)
        self._session.add(new_obj)
        self._session.flush()
        return new_obj

    def update(self, obj: T, update: U) -> T:
        obj = super().update(obj, update)
        self._session.add(obj)
        self._session.flush()
        return obj

    def delete(self, obj: T) -> T:
        self._session.delete(obj)
        self._session.flush()
        return obj
