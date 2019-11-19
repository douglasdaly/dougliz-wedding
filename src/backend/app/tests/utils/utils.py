# -*- coding: utf-8 -*-
"""
Misc. utilities for tests.
"""
import random
import string

import requests

from app.core import config


def random_lower_string():
    return "".join(random.choices(string.ascii_lowercase, k=32))


def get_server_api():
    server_name = "http://"
    if config.SERVER_NAME:
        server_name += f"{config.SERVER_NAME}"
    else:
        server_name += f"{config.SERVER_HOST}"
        if config.SERVER_PORT:
            server_name += f":{config.SERVER_PORT}"
    return server_name + "/api/"


def get_superuser_token_headers():
    server_api = get_server_api()
    login_data = {
        "username": config.SUPERUSER_EMAIL,
        "password": config.SUPERUSER_PASSWORD,
    }
    r = requests.post(
        f"{server_api}{config.API_VERSION}/login/access-token",
        data=login_data
    )
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers
