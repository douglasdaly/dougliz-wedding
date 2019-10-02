# -*- coding: utf-8 -*-
"""
Access token model.
"""
from pydantic import BaseModel


class Token(BaseModel):
    """
    Access Token
    """
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    """
    Payloads for Tokens
    """
    user_id: int = None
