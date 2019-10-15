# -*- coding: utf-8 -*-
"""
Wedding API endpoints.
"""
from fastapi import APIRouter

from app.api.v1.endpoints.wedding import wedding_info


# Wedding API router config
router = APIRouter()
router.include_router(wedding_info.router, prefix="/info")
