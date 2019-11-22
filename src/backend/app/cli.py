#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Application CLI tools.
"""
from collections import defaultdict
import copy
from datetime import datetime, timedelta
import logging
import os
import sys
import threading
import traceback
import typing as tp

import click
from tenacity import (
    retry,
    stop_after_attempt,
    wait_fixed
)
import uvicorn

# - Append Python path for app development
APP_PATH = os.path.abspath(
    os.path.join(__file__, os.path.pardir, os.path.pardir)
)
if APP_PATH not in sys.path:
    sys.path.append(APP_PATH)

from app.core import config  # noqa: E402
from app.db.session import db_session  # noqa: E402
import app.db.utils as db_utils  # noqa: E402
from app.main import app as fastapi_app  # noqa: E402
from app.tests.api.v1.endpoints.test_login import (  # noqa: E402
    test_get_access_token
)


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

DEPTH_STYLES = defaultdict(lambda: dict(dim=True))
DEPTH_STYLES[0] = {}


#
#   Setup & Helpers
#

logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)


def get_log_fn(
    component: tp.Optional[str] = None,
    initial_depth: tp.Optional[int] = None,
    print_out: tp.Optional[bool] = None,
    log_out: tp.Optional[bool] = None,
    verbose: tp.Optional[bool] = None
) -> tp.Callable:
    """Gets a helper log function for component logging."""
    if not component:
        component = click.get_current_context().info_name.upper()
    else:
        component = component.upper()
    if initial_depth is None:
        initial_depth = click.get_current_context().obj.get("log_level", 0)
    if print_out is None:
        print_out = click.get_current_context().obj.get("is_printing", True)
    if log_out is None:
        log_out = click.get_current_context().obj.get("is_logging", False)
    if verbose is None:
        verbose = click.get_current_context().obj.get("verbose", False)

    def _log_fn(
        msg: tp.Union[str, Exception],
        level: int = logging.INFO,
        depth: int = 0,
        depth_spacer: str = '-',
        level_style: tp.Optional[tp.Mapping] = None,
        depth_style: tp.Optional[tp.Mapping] = None
    ) -> None:
        depth = initial_depth + depth
        spacer = f" {depth_spacer * depth}{' ' if depth > 0 else ''}"

        if level_style is None:
            level_style = LEVEL_STYLES.get(level, {})
        if depth_style is None:
            depth_style = DEPTH_STYLES[depth]

        msg_pre = click.style(f"[{component:^5}]", **level_style)
        msg_post = click.style(f"{spacer}{msg!s}", **depth_style)
        full_msg = msg_pre + msg_post

        if print_out:
            click.echo(full_msg)
        if log_out:
            logging.log(level, click.unstyle(full_msg))
        if verbose and isinstance(msg, Exception):
            full_err = traceback.format_exc()
            if print_out:
                click.echo(full_err)
            if log_out:
                logging.log(level, full_err)
        return

    return _log_fn


class StoppableThread(threading.Thread):
    """
    Thread class with a (graceful) stop ability.
    """

    def __init__(self, *args, **kwargs) -> None:
        self._stop_flag = threading.Event()
        return super().__init__(*args, **kwargs)

    def signal_stop(self) -> None:
        """Requests that this thread stop execution."""
        if not self.stop_received:
            self._stop_flag.set()
        return

    def stop_received(self) -> bool:
        """Whether or not this thread is stopped."""
        return self._stop_flag.is_set()


def run_command_thread(
    ctx: click.Context,
    command: click.Command,
    *,
    args: tp.Optional[tp.Iterable] = None,
    kwargs: tp.Optional[tp.Mapping] = None,
    **ctx_updates
) -> StoppableThread:
    """Creates a thread for the given command to run in.

    Parameters
    ----------
    ctx : click.Context
        The click context object to use.
    command : click.Command
        The click command to invoke in a new thread.
    args : Iterable, optional
        The arguments to pass to the `command` given.
    kwargs : Mapping, optional
        The keyword-arguments to pass to the `command` given.
    **ctx_updates : optional
        Any temporary context variables to set in the child thread's
        context.

    Returns
    -------
    StoppableThread
        The (started) thread invoking the specified `command`.

    """
    if args is None:
        args = tuple()
    if kwargs is None:
        kwargs = {}

    local_obj = copy.deepcopy(ctx.obj)
    if ctx_updates is not None:
        local_obj.update(ctx_updates)

    def _wrapper():
        local_ctx = click.Context(
            command, info_name=command.name, parent=ctx,
            obj=local_obj
        )

        new_kws = kwargs.copy()
        for p in command.params:
            if p.name not in new_kws and p.expose_value:
                new_kws[p.name] = p.get_default(local_ctx)

        with local_ctx:
            return command.callback(*args, **new_kws)

    rv = StoppableThread(target=_wrapper)
    rv.start()
    return rv


@retry(
    stop=stop_after_attempt(MAX_TRIES),
    wait=wait_fixed(WAIT_SECONDS)
)
def _check_api(log_fn: tp.Callable) -> None:
    """See if the API is alive."""
    try:
        log_fn('Attempting to get Access Token', depth=1)
        test_get_access_token()
    except Exception as ex:
        log_fn(ex, level=logging.WARN)
        raise ex
    return True


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
    return True


#
#   Script Functions
#

CONTEXT_SETTINGS = {
    'ignore_unknown_options': True,
    'allow_extra_args': True,
}


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--verbose', is_flag=True, default=False, help="Verbose output")
@click.pass_context
def cli(ctx, verbose) -> None:
    """
    Backend application CLI tools.
    """
    ctx.ensure_object(dict)
    ctx.obj['is_printing'] = True
    ctx.obj['is_logging'] = False
    ctx.obj['log_level'] = 0
    ctx.obj['verbose'] = verbose
    return


# Configuration

@cli.group('config', chain=True, invoke_without_command=True)
@click.pass_context
def config_grp(ctx, **kwargs) -> None:
    """
    Configuration tools.
    """
    if ctx.invoked_subcommand is None:
        return ctx.forward(config_list)
    return


@config_grp.command('list')
@click.argument('section', nargs=-1, type=click.STRING)
@click.option('--show-hidden', is_flag=True, default=False,
              help="Display sensitive values", show_default=True)
@click.pass_context
def config_list(
    ctx,
    section: tp.Optional[str],
    show_hidden: bool
) -> None:
    """Displays current configuration settings."""
    disp_groups = {
        'General': [
            'PROJECT_NAME',
            'DEBUG',
        ],
        'API': [
            'API_VERSION',
            'SERVER_NAME',
            'SERVER_HOST',
            'SERVER_PORT',
        ],
        'Security': [
            'SECRET_KEY',
            'ALLOWED_ORIGINS',
            'ACCESS_TOKEN_EXPIRE_MINUTES',
            'EMAIL_RESET_TOKEN_EXPIRE_HOURS',
        ],
        'Storage': [
            'STORAGE_TYPE',
            'DB_ENGINE',
            'DB_DRIVER',
            'DB_HOST',
            'DB_PORT',
            'DB_NAME',
            'DB_USER',
            'DB_PASSWORD',
            'DB_CONNECT_EXTRA',
        ],
        'Emails': [
            'EMAILS_ENABLED',
            'EMAILS_FROM_EMAIL',
            'EMAILS_FROM_NAME',
            'EMAILS_TEMPLATE_DIR',
            'SMTP_HOST',
            'SMTP_PORT',
            'SMTP_TLS',
            'SMTP_USER',
            'SMTP_PASSWORD',
        ],
        'Users': [
            'USERS_OPEN_REGISTRATION',
            'SUPERUSER_EMAIL',
            'SUPERUSER_PASSWORD',
        ]
    }
    hidden = {
        'Security': [
            'SECRET_KEY',
        ],
        'Storage': [
            'DB_HOST',
            'DB_PORT',
            'DB_USER',
            'DB_PASSWORD',
            'DB_CONNECT_EXTRA',
        ],
        'Emails': [
            'SMTP_HOST',
            'SMTP_PORT',
            'SMTP_TLS',
            'SMTP_USER',
            'SMTP_PASSWORD',
        ],
        'Users': [
            'SUPERUSER_EMAIL',
            'SUPERUSER_PASSWORD',
        ]
    }

    if not section:
        section = sorted(disp_groups.keys())
    else:
        cln_sects = [x.lower() for x in section]
        section = []
        for s in sorted(disp_groups.keys()):
            if s.lower() in cln_sects:
                section.append(s)

    lines = []
    for s in section:
        lines.append(click.style(f"[{s}]", bold=True))
        for v in disp_groups[s]:
            t_val = getattr(config, v, None)
            if t_val is None:
                t_val = click.style('<Unset>', dim=True)
            elif v in hidden.get(s, ()) and not show_hidden:
                t_val = click.style('<Hidden>', dim=True)

            t_line = '  ' + click.style(f'{v:<30}', fg='cyan', bold=True)
            t_line += f'\t{t_val}'
            lines.append(t_line)

    to_print = '\n'.join(lines)
    click.echo(to_print)
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
@click.password_option(prompt=config.SUPERUSER_PASSWORD is None)
@click.option('--use-alembic', type=click.BOOL, default=False,
              help="Use Alembic to perform the initialization",
              show_default=True)
@click.pass_context
def init_db(
    ctx,
    email: tp.Optional[str] = None,
    password: tp.Optional[str] = None,
    use_alembic: tp.Optional[bool] = None
) -> None:
    """Initializes the database."""
    _db_log = get_log_fn()
    _db_log('Initializing database')
    ctx.obj['log_level'] += 1

    _db_log("Creating database", depth=1)
    db_utils.create_database(use_alembic=use_alembic)

    _db_log("Creating initial superuser", depth=1)
    db_utils.create_initial_superuser(db_session, su_email=email,
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
    if _check_db(_chk_log):
        _chk_log('Database available')
    else:
        _chk_log('Database unavailable', level=logging.WARN)
    return



@check.command('api')
@click.pass_context
def check_api(ctx) -> None:
    """
    Checks if the API service is up and available.
    """
    _chk_log = get_log_fn(verbose=True)
    _chk_log('Checking API service')
    if _check_api(_chk_log):
        _chk_log('API service available')
    else:
        _chk_log('API service unavailable', level=logging.WARN)
    return


@check.command('all')
@click.pass_context
def check_all(ctx, **kwargs) -> None:
    """Main script function."""
    _chk_log = get_log_fn()
    _chk_log("Checking services")

    # - Database
    ctx.invoke(check_db, **kwargs)
    ctx.invoke(check_api, **kwargs)

    _chk_log("All checks passed")
    return


# Running

@cli.group(invoke_without_command=True)
@click.pass_context
def run(ctx, **kwargs) -> None:
    """
    Run components.
    """
    if ctx.invoked_subcommand is None:
        return ctx.forward(run_all)
    return


@run.command('api')
@click.argument('wsgi-server', nargs=-1, type=click.STRING,
                envvar="API_WSGI_SERVER")
@click.option('--port', type=click.INT, default=os.getenv("API_PORT", 5000),
              show_default=True, help="Port for the API to listen on.")
@click.option('--log-level', default="warning", help="Logging level to use.")
@click.option('--skip-checks', is_flag=True, default=False,
              help="Skip pre-start checks.")
@click.pass_context
def run_api(ctx, wsgi_server, port, log_level, skip_checks) -> None:
    """
    Runs the FastAPI application via WSGI.
    """
    _run_log = get_log_fn()

    # - Arg handling
    log_level = log_level.strip().lower()

    # - Pre-start checks
    if not skip_checks:
        _run_log("Running pre-start checks:")
        ctx.obj["log_level"] += 1

        # - Database
        try:
            ctx.invoke(check_db)
            _run_log("Database: PASSED", depth=1)
        except Exception as ex:
            _run_log("Database: ERROR", level=logging.ERROR, depth=1)
            raise ex

        ctx.obj["log_level"] -= 1
    else:
        _run_log("Skipping pre-start checks", level=logging.WARN)

    # - Run server
    _run_log("Launching API")
    if not wsgi_server:
        _run_log("No WSGI server specified (using: uvicorn)", depth=1)
        wsgi_server = 'uvicorn'
    else:
        wsgi_server = wsgi_server.strip().lower()

    if wsgi_server == 'uvicorn':
        _run_log("Starting uvicorn server")
        _run_log("(Press CTRL-C to stop)", depth_style={'dim': True})
        uvicorn.run(
            fastapi_app,
            host='127.0.0.1',
            port=port,
            log_level=log_level
        )
        click.secho()
    else:
        _run_log(f"Unsupported WSGI Server: {wsgi_server}",
                 level=logging.ERROR)
    return


@run.command('all')
@click.pass_context
def run_all(ctx, **kwargs):
    """
    Runs all the application components.
    """
    _run_log = get_log_fn()
    _run_log('Starting all components:')
    ctx.obj["log_level"] += 1

    p_threads = {}

    # - API (this thread, last)
    ctx.invoke(run_api, **kwargs)
    click.echo()

    if p_threads:
        _run_log(f'Sending stop to {len(p_threads)} threads:')
        for k, v in p_threads.items():
            v.stop()
            _run_log(f"SIGNALED: {k}", depth=1)

        _run_log('Waiting for components to end:')
        to_remove = []
        timeout_end = datetime() + timedelta(seconds=30)
        while p_threads or datetime.now() <= timeout_end:
            to_remove.clear()
            for k, v in p_threads.items():
                if not v.is_alive():
                    v.join()
                    _run_log(f"STOPPED: {k}", depth=1)
                    to_remove.append(k)
            for k in to_remove:
                p_threads.pop(k)

    ctx.obj["log_level"] -= 1
    return


#
#   Entry-point
#

if __name__ == "__main__":
    cli(obj={})
