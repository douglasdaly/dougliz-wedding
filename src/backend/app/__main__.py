#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys


APP_PATH = os.path.abspath(
    os.path.join(__file__, os.path.pardir, os.path.pardir)
)
if APP_PATH not in sys.path:
    sys.path.append(APP_PATH)

from app.cli import cli  # noqa: E402


if __name__ == '__main__':
    cli(obj={})
