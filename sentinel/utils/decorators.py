import inspect
import time

import typer


def manage_warnings(func):
    def inner(*args,**kwargs):
        if args[-1]:
            typer.secho("\n\n[Warning] Force is enabled\n",fg=typer.colors.YELLOW)
        func(*args,**kwargs)
    return inner
