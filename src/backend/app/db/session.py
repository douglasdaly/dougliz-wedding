# -*- coding: utf-8 -*-
"""
Database Session-related objects.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from app.core import config


engine = create_engine(
    config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True,
    connect_args=config.DB_CONNECT_EXTRA
)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
