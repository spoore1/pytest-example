from utils import ssh_pexpect

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--username", action="store", default="testuser1",
        help="User to use for ssh remote tests"
    )
    parser.addoption(
        "--password", action="store", default="u5erP@ss1",
        help="password for user for ssh connections"
    )
    parser.addoption(
        "--hostname", action="store", default="localhost",
        help="User to use for ssh remote tests"
    )

@pytest.fixture
def username(request):
    return request.config.getoption("--username")

@pytest.fixture
def password(request):
    return request.config.getoption("--password")

@pytest.fixture
def hostname(request):
    return request.config.getoption("--hostname")
