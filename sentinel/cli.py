"""This module provides the RP To-Do CLI."""

from typing import Optional

import typer

from . import __app_name__, __version__, __host_url__, ERRORS
from .auth import Auth
from .core import ScriptGen
from .ctyper.Typer import CTyper
from .utils.decorators import manage_warnings
from .utils.loader import Loader

app = CTyper()


@app.command()
def init():
    ScriptGen().scan().add_each()


@app.command()
def login(
        access_token: str = typer.Option(
            Auth().get_access_token(),
            help=f"go to  {__host_url__}/access_keys to generate the key corresponding to this monitor",
            prompt="Access token ",
        ), force: Optional[bool] = typer.Option(
            None,
            "--force",
            "-f",
            help="Clear the pre-fetched access_token",

        )
) -> None:
    Auth().login(access_token, force)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")

        raise typer.Exit()


@app.callback()
def main(
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            "-v",
            help="Show the application's version and exit.",
            callback=_version_callback,
            is_eager=True,

        )

) -> None:
    # print(version)
    return
