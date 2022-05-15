"""This module provides the RP To-Do CLI."""

# rptodo/cli.py


from typing import Optional

import typer

from . import __app_name__, __version__, __host_url__, ERRORS
from .auth import Auth

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")

        raise typer.Exit()


@app.command()
def login(
        access_token: str = typer.Option(
            Auth().get_access_token(),
            help=f"go to  {__host_url__}/access_keys to generate the key corresponding to this monitor",
            prompt="Access token for authorization:\n",
        ),
) -> None:
    login_ret = Auth().login(access_token)

    if login_ret:
        typer.secho(
            f'login failed with "{ERRORS[login_ret]}"',
            fg=typer.colors.RED,
        )

    return


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
