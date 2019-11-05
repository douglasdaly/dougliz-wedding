# -*- coding: utf-8 -*-
"""
Core functionality for the actions module.
"""
from sqlalchemy.orm import Session

from app.crud.core import UnitOfWork
from app.utils.proputils import lazy_property

from app.db.crud.address import AddressSQLRepository
from app.db.crud.contact_info import ContactInfoSQLRepository
from app.db.crud.event import EventSQLRepository
from app.db.crud.name import NameSQLRepository
from app.db.crud.person import PersonSQLRepository
from app.db.crud.user import UserSQLRepository

from app.db.crud.config.core import ConfigSQLRepositoryGroup
from app.db.crud.wedding.core import WeddingSQLRepositoryGroup


class SQLUnitOfWork(UnitOfWork):
    """
    Unit of Work base class for actions.

    Parameters
    ----------
    db_session : Session
        The database session object to use for this interaction.

    """
    __slots__ = ('_session',)

    def __init__(self, db_session: Session) -> None:
        self._session = db_session
        return super().__init__()

    # Repositories

    @lazy_property
    def address(self) -> AddressSQLRepository:
        return AddressSQLRepository(self, self._session)

    @lazy_property
    def contact_info(self) -> ContactInfoSQLRepository:
        return ContactInfoSQLRepository(self, self._session)

    @lazy_property
    def event(self) -> EventSQLRepository:
        return EventSQLRepository(self, self._session)

    @lazy_property
    def name(self) -> NameSQLRepository:
        return NameSQLRepository(self, self._session)

    @lazy_property
    def person(self) -> PersonSQLRepository:
        return PersonSQLRepository(self, self._session)

    @lazy_property
    def user(self) -> UserSQLRepository:
        return UserSQLRepository(self, self._session)

    # Repository groups

    @lazy_property
    def wedding(self) -> WeddingSQLRepositoryGroup:
        return WeddingSQLRepositoryGroup(self, self._session)

    @lazy_property
    def config(self) -> ConfigSQLRepositoryGroup:
        return ConfigSQLRepositoryGroup(self, self._session)

    # Commit/rollback

    def commit(self) -> None:
        return self._session.commit()

    def rollback(self) -> None:
        return self._session.rollback()
