import requests
import typer
from requests_mock.mocker import Mocker
from typer.testing import CliRunner

from sentinel import __app_name__, __version__, cli, __host_url__
from sentinel.utils.cron import add_to_crontab, EVEN_HOUR
import os
runner = CliRunner()


def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout


def test_authentication_login_successful_response(requests_mock: Mocker):
    url = f"{__host_url__}/auth/monitor/"
    requests_mock.post(url, status_code=200, json={
        "access_token": 'test_access_token',
    })
    result = runner.invoke(cli.app, ['login', '--access-token', 'test_access_token'])
    assert 'Successful' == result.stdout.strip().split(' ')[-1]


def test_authentication_login_failed_response(requests_mock: Mocker):
    url = f"{__host_url__}/auth/monitor/"
    requests_mock.post(url, status_code=403, json={
        "status": 'failed',
    })
    result = runner.invoke(cli.app, ['login', '--access-token', 'test_access_token'])
    assert not 'Successful' == result.stdout.strip().split(' ')[-1]

