# -*- coding: utf-8 -*-
"""
JSON utilities.
"""
import json
from uuid import UUID


class JSONEncoderUUID(json.JSONEncoder):
    """
    JSON Encoder with UUID support.
    """

    def default(self, obj):
        if isinstance(obj, UUID):
            return obj.hex
        return super().default(obj)
