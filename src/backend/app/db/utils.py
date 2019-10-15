# -*- coding: utf-8 -*-
"""
Database utilities.
"""
import typing as tp

from sqlalchemy.orm import Session

from app.core import config
from app.db.crud.core import SQLUnitOfWork
from app.db.session import engine
from app.models.user import UserCreate

# Ensure all SqlAlchemy models are imported before initializing the DB.
from app.db import base  # noqa: F401


def initialize_database(
    db_session: Session,
    *,
    use_alembic: bool = True
) -> None:
    """Initializes the database.

    Parameters
    ----------
    db_session : Session
        The database session to use.
    use_alembic : bool, optional
        Use Alembic for database schema change management (default is
        ``True``).

    """
    if not use_alembic:
        base.Base.metadata.create_all(bind=engine)
    return


def create_initial_superuser(
    db_session: Session,
    *,
    su_email: tp.Optional[str] = None,
    su_password: tp.Optional[str] = None
) -> None:
    """Creates the initial superuser account.

    Parameters
    ----------
    db_session : Session
        The database session to use.
    su_email : str, optional
        The email address to use for the first superuser account (if not
        given then :obj:`config.SUPERUSER_EMAIL` is used).
    su_password : str, optional
        The password to use for the first superuser account (if not
        given then :obj:`config.SUPERUSER_PASSWORD` is used).

    """
    if not su_email:
        su_email = config.SUPERUSER_EMAIL
    uow = SQLUnitOfWork(db_session)
    user = uow.user.get_by_email(su_email)
    if not user:
        if not su_password:
            su_password = config.SUPERUSER_PASSWORD
        new_super_user = UserCreate(email=su_email, password=su_password)
        new_super_user.is_poweruser = True
        new_super_user.is_superuser = True
        with uow:
            user = uow.user.create(new_super_user)
    return
