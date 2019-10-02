# -*- coding: utf-8 -*-
"""
Message model.
"""
from pydantic import BaseModel


class Message(BaseModel):
    """
    Message object model.
    """
    value: str
