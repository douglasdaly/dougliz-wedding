# -*- coding: utf-8 -*-
"""
API for application settings and permissions objects.
"""
from fastapi import APIRouter

from app.api.v1.endpoints.config import settings


# Settings API router config
router = APIRouter()
router.include_router(settings.router, prefix="/settings")
