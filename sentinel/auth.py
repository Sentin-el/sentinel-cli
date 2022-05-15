from typing import Optional

from . import (
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    AUTHORIZATION_ERROR,
    __host_url__
)
import requests


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

    def login(self, access_token: str) -> int:

        response = requests.post(self.url, data={'access_token': access_token, })
        # let the response be
        if response.status_code == 200:
            # self.put_access_token(response.body.access_token)
            return SUCCESS
        else:

            return AUTHORIZATION_ERROR

    def get_access_token(self) -> Optional[str]:
        self.auth_file = "/home/dps/.sentinel/ACCESS_TOKEN"
        ret = None
        try:
            with open(self.auth_file, "r") as f:
                return f.read().strip()
        except FileNotFoundError as e:
            return None

    def put_access_token(self, access_token) -> None:
        with open(self.auth_file, "w") as f:
            f.write(access_token)
