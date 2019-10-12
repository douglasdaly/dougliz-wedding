# -*- coding: utf-8 -*-
"""
Access token model.
"""
from typing import Optional
from uuid import UUID

from app.models.base import AppBaseModel


class Token(AppBaseModel):
    """
    Access Token
    """
    access_token: str
    token_type: str


class TokenPayload(AppBaseModel):
    """
    Payloads for Tokens
    """
    user_id: Optional[UUID] = None
