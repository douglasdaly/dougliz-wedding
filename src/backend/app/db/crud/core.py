# -*- coding: utf-8 -*-
"""
Core functionality for the actions module.
"""
from sqlalchemy.orm import Session

from app.crud.core import UnitOfWork
from app.db.crud.address import AddressSQLRepository
from app.db.crud.contact_info import ContactInfoSQLRepository
from app.db.crud.name import NameSQLRepository
from app.db.crud.person import PersonSQLRepository
from app.db.crud.user import UserSQLRepository
from app.utils.proputils import lazy_property


class SQLUnitOfWork(UnitOfWork):
    """
    Unit of Work base class for actions.

    Parameters
    ----------
    db_session : Session
        The database session object to use for this interaction.

    """

    def __init__(self, db_session: Session) -> None:
        self._session = db_session
        return super().__init__()

    @lazy_property
    def address(self) -> AddressSQLRepository:
        return AddressSQLRepository(self, self._session)

    @lazy_property
    def contact_info(self) -> ContactInfoSQLRepository:
        return ContactInfoSQLRepository(self, self._session)

    @lazy_property
    def name(self) -> NameSQLRepository:
        return NameSQLRepository(self, self._session)

    @lazy_property
    def person(self) -> PersonSQLRepository:
        return PersonSQLRepository(self, self._session)

    @lazy_property
    def user(self) -> UserSQLRepository:
        return UserSQLRepository(self, self._session)

    def commit(self) -> None:
        return self._session.commit()

    def rollback(self) -> None:
        return self._session.rollback()
