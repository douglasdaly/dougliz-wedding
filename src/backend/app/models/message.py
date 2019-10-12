# -*- coding: utf-8 -*-
"""
Message model.
"""
from app.models.base import AppBaseModel


class Message(AppBaseModel):
    """
    Message object model.
    """
    value: str
