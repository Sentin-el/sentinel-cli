from typing import Optional

import typer

from . import (
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    AUTHORIZATION_ERROR,
    __host_url__, ERRORS
)
import requests

from .utils.decorators import manage_warnings
from .utils.loader import Loader


class AuthMetaClass(type):
    def __init__(cls, *args, **kwargs):
        cls.__single_instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__single_instance:
            return cls.__single_instance
        single_obj = cls.__new__(cls)
        single_obj.__init__(*args, **kwargs)
        cls.__single_instance = single_obj
        return single_obj


class Auth(metaclass=AuthMetaClass):
    def __init__(self):
        self.auth_file = "/home/dps/.sentinel/ACCESS_TOKEN"
        self.url = f"{__host_url__}/auth/monitor/"
        self.auth_token = None

    @manage_warnings
    def login(self, access_token: str, force=False) -> int:
        with Loader("Authorizing...", "\n", 0.05) as l:
            if (not self.auth_token) or force:
                response = requests.post(self.url, data={'access_token': access_token, })
                if response.status_code == 200:
                    # self.put_access_token(response.body.access_token)

                    self.auth_token = response.json()['access_token']
                    typer.secho(
                        '\nLogin Successful',
                        fg=typer.colors.GREEN,
                    )
                else:
                    typer.secho(
                        f'\nLogin failed with "{ERRORS[AUTHORIZATION_ERROR]}"',
                        fg=typer.colors.RED,
                    )

            return SUCCESS

    def get_access_token(self) -> Optional[str]:
        self.auth_file = "/home/dps/.sentinel/ACCESS_TOKEN"
        ret = None
        if self.auth_token:
            return self.auth_token
        try:
            with open(self.auth_file, "r") as f:
                return f.read().strip()
        except FileNotFoundError as e:
            return None

    def put_access_token(self, access_token) -> None:
        with open(self.auth_file, "w") as f:
            f.write(access_token)
