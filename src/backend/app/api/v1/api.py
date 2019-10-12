# -*- coding: utf-8 -*-
"""
API specification for v1 of the backend.
"""
from fastapi import APIRouter

from app.api.v1.endpoints import addresses
from app.api.v1.endpoints import login
from app.api.v1.endpoints import names
from app.api.v1.endpoints import people
from app.api.v1.endpoints import users

# Router config
api_router = APIRouter()
api_router.include_router(addresses.router, prefix="/addresses",
                          tags=["addresses"])
api_router.include_router(login.router, prefix="/login", tags=["login"])
api_router.include_router(names.router, prefix="/names", tags=["names"])
api_router.include_router(people.router, prefix="/people", tags=["people"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
