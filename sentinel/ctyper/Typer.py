from typing import Optional, Type, Dict, Any, Callable

import click
from typer import Typer
from typer.core import TyperCommand
from typer.models import CommandFunctionType, CommandInfo

from sentinel.utils.decorators import manage_warnings


class CTyper(Typer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
