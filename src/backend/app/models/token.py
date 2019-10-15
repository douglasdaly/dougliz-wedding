# -*- coding: utf-8 -*-
"""
Access token model.
"""
from typing import Optional
from uuid import UUID

from app.models.base import AppBaseModel
from app.models.base import get_custom_getter


class Token(AppBaseModel):
    """
    Access Token
    """
    access_token: str
    token_type: str

    class Config:
        fields = {
            'access_token': 'accessToken',
            'token_type': 'tokenType',
        }


class TokenPayload(AppBaseModel):
    """
    Payloads for Tokens
    """
    user_id: Optional[UUID] = None
