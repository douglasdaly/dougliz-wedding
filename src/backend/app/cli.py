#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Application CLI tools.
"""
import logging
import os
import sys
import typing as tp

import click
from tenacity import (
    retry,
    stop_after_attempt,
    wait_fixed
)

# - Append Python path for app
APP_PATH = os.path.abspath(
    os.path.join(__file__, os.path.pardir, os.path.pardir)
)
if APP_PATH not in sys.path:
    sys.path.append(APP_PATH)

from app.db import utils  # noqa: E402
from app.db.session import db_session  # noqa: E402


#
#   Configuration
#

MAX_TRIES = 60 * 5  # 5 minutes
WAIT_SECONDS = 1

LOG_LEVEL = logging.INFO

# Styling
LEVEL_STYLES = {
    logging.DEBUG: dict(fg='cyan'),
    logging.INFO: dict(bold=True),
    logging.WARN: dict(fg='yellow', bold=True),
    logging.ERROR: dict(fg='red', bold=True),
}

DEPTH_STYLES = {
    1: dict(dim=True),
}


#
#   Setup & Helpers
#

logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)


def get_log_fn(
    component: tp.Optional[str] = None,
    initial_depth: tp.Optional[int] = None,
    log_out: tp.Optional[bool] = None
) -> tp.Callable:
    """Gets a helper log function for component logging."""
    if not component:
        component = click.get_current_context().info_name.upper()
    else:
        component = component.upper()
    if initial_depth is None:
        initial_depth = click.get_current_context().obj.get("log_level", 0)
    if log_out is None:
        log_out = click.get_current_context().obj.get("log_out", False)

    def _log_fn(
        msg: str,
        level: int = logging.INFO,
        depth: int = 0,
        depth_spacer: str = '-'
    ) -> None:
        depth = initial_depth + depth
        spacer = f" {depth_spacer * depth}{' ' if depth > 0 else ''}"
        msg_pre = click.style(f"[{component:^5}]",
                              **LEVEL_STYLES.get(level, {}))
        msg_post = click.style(
            f"{spacer}{msg!s}", **DEPTH_STYLES.get(depth, {})
        )
        full_msg = msg_pre + msg_post

        click.echo(full_msg)
        if log_out:
            logging.log(level, click.unstyle(full_msg))
        return

    return _log_fn


@retry(
    stop=stop_after_attempt(MAX_TRIES),
    wait=wait_fixed(WAIT_SECONDS)
)
def _check_db(log_fn: tp.Callable) -> None:
    """See if the database is alive."""
    try:
        log_fn('Executing SELECT', depth=1)
        db_session.execute("SELECT 1")
    except Exception as ex:
        log_fn(ex, level=logging.WARN)
        raise ex
    return


#
#   Script Functions
#

CONTEXT_SETTINGS = {
    'ignore_unknown_options': True,
    'allow_extra_args': True,
}


@click.group(context_settings=CONTEXT_SETTINGS)
@click.pass_context
def cli(ctx) -> None:
    """
    Backend application CLI tools.
    """
    ctx.ensure_object(dict)
    ctx.obj['log_level'] = 0
    return


# Initialization

@cli.group(chain=True, invoke_without_command=True)
@click.pass_context
def init(ctx, **kwargs) -> None:
    """
    Initialization tools.
    """
    if ctx.invoked_subcommand is None:
        return ctx.forward(init_all)
    return


@init.command("db")
@click.option('--email', type=click.STRING, default=None,
              help="Email address to use for the initial superuser account.")
@click.password_option()
@click.pass_context
def init_db(
    ctx,
    email: tp.Optional[str] = None,
    password: tp.Optional[str] = None
) -> None:
    """Initializes the database."""
    _db_log = get_log_fn()
    _db_log('Initializing database')
    ctx.obj['log_level'] += 1

    _db_log("Creating database", depth=1)
    utils.initialize_database(db_session, use_alembic=False)

    _db_log("Creating initial superuser", depth=1)
    utils.create_initial_superuser(db_session, su_email=email,
                                   su_password=password)

    ctx.obj['log_level'] -= 1
    return


@init.command("all")
@click.pass_context
def init_all(ctx, **kwargs) -> None:
    """Main script call."""
    _log_all = get_log_fn()
    _log_all('Initializing all components')

    # - Database
    ctx.invoke(init_db, **kwargs)

    _log_all("Initialization complete")
    return


# Checks

@cli.group(chain=True, invoke_without_command=True)
@click.pass_context
def check(ctx, **kwargs) -> None:
    """
    Component checks.
    """
    if ctx.invoked_subcommand is None:
        return ctx.forward(check_all)
    return


@check.command('db')
@click.pass_context
def check_db(ctx) -> None:
    """
    Checks if the database is up and available.
    """
    _chk_log = get_log_fn()
    _chk_log('Checking database')
    return _check_db(_chk_log)


@check.command('all')
@click.pass_context
def check_all(ctx, **kwargs) -> None:
    """Main script function."""
    _chk_log = get_log_fn()
    _chk_log("Initializing services")

    # - Database
    ctx.invoke(check_db, **kwargs)

    _chk_log("All services initialized")
    return


#
#   Entry-point
#

if __name__ == "__main__":
    cli(obj={})
