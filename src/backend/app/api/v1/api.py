# -*- coding: utf-8 -*-
"""
API specification for v1 of the backend.
"""
from fastapi import APIRouter

from app.api.v1.endpoints import login
from app.api.v1.endpoints import users


api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(login.router, prefix="/login", tags=["login"])
