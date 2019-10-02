# -*- coding: utf-8 -*-
"""
Main backend API components.
"""
import typing as tp

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response

from app.api.utils.core import load_api_router
from app.core import config
from app.db.session import Session


app = FastAPI(title=config.PROJECT_NAME, openapi_url="/api/openapi.json")


# CORS
origins = []

if config.ALLOWED_ORIGINS:
    origins_raw = config.ALLOWED_ORIGINS.split(',')
    for origin in origins_raw:
        origins.append(origin.strip())

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )


api_router = load_api_router(config.API_VERSION)
app.include_router(api_router, prefix=f"/api")


@app.middleware('http')
async def db_session_middleware(
    request: Request,
    call_next: tp.Callable
) -> Response:
    """Middleware to add database session to request state."""
    request.state.db = Session()
    response = await call_next(request)
    request.state.db.close()
    return response
