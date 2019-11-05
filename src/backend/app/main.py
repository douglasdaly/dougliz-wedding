# -*- coding: utf-8 -*-
"""
Main backend API components.
"""
import typing as tp

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.responses import Response
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND
)

from app.api.utils.core import load_api_router
from app.core import config
from app.db.crud.core import SQLUnitOfWork
from app.db.session import Session
from app.exceptions import (
    APIError,
    ObjectNotFoundError,
    ObjectExistsError,
    PrivilegeError,
)


app = FastAPI(title=config.PROJECT_NAME, openapi_url="/api/openapi.json")


# Security

# - HTTPS
if not config.DEBUG:
    app.add_middleware(HTTPSRedirectMiddleware)

# - CORS
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


# API Routes Configuration

api_router = load_api_router(config.API_VERSION)
app.include_router(api_router, prefix=f"/api")


# Additional Middleware (order matters)

@app.middleware('http')
async def uow_middleware(
    request: Request,
    call_next: tp.Callable
) -> Response:
    """Middleware to add session-based Unit of Work to request state."""
    request.state.uow = SQLUnitOfWork(request.state.db)
    response = await call_next(request)
    return response


@app.middleware('http')
async def db_session_middleware(
    request: Request,
    call_next: tp.Callable
) -> Response:
    """Middleware to add database session object to request state."""
    request.state.db = Session()
    response = await call_next(request)
    request.state.db.close()
    return response


# Additional Error Handlers

@app.exception_handler(APIError)
async def api_exception_handler(
    request: Request,
    exc: APIError
) -> JSONResponse:
    """API exception handler."""
    return JSONResponse({'message': str(exc)},
                        status_code=HTTP_400_BAD_REQUEST)


@app.exception_handler(ObjectExistsError)
async def object_exists_exception_handler(
    request: Request,
    exc: ObjectExistsError
) -> JSONResponse:
    """Object already exists exception handler."""
    return JSONResponse({'message': str(exc)},
                        status_code=HTTP_400_BAD_REQUEST)


@app.exception_handler(ObjectNotFoundError)
async def object_not_found_exception_handler(
    request: Request,
    exc: ObjectNotFoundError
) -> JSONResponse:
    """Object does not exist exception handler."""
    return JSONResponse({'message': str(exc)}, status_code=HTTP_404_NOT_FOUND)


@app.exception_handler(PrivilegeError)
async def privilege_exception_handler(
    request: Request,
    exc: PrivilegeError
) -> JSONResponse:
    """Insufficient privileges exception handler."""
    return JSONResponse({'message': str(exc)}, status_code=HTTP_403_FORBIDDEN)
