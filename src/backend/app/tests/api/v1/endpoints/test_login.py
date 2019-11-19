# -*- coding: utf-8 -*-
"""
Unit tests for /login API endpoints.
"""
import requests

from app.core import config
from app.tests.utils.utils import get_server_api


def test_get_access_token() -> None:
    server_api = get_server_api()
    login_url = f"{server_api}{config.API_VERSION}/login/access-token"
    login_data = {
        "username": config.SUPERUSER_EMAIL,
        "password": config.SUPERUSER_PASSWORD,
    }

    r = requests.post(login_url, data=login_data)
    assert r.status_code == 200
    assert r.text is not None and r.text != ''

    tokens = r.json()
    assert "access_token" in tokens
    assert tokens["access_token"]

    return


def test_use_access_token(superuser_token_headers) -> None:
    server_api = get_server_api()
    r = requests.post(
        f"{server_api}{config.API_VERSION}/login/test-token",
        headers=superuser_token_headers,
    )
    result = r.json()
    assert r.status_code == 200
    assert "email" in result

    return
