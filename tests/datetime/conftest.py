import pytest
from brownie import accounts, DateTime

@pytest.fixture(scope="session")
def crontab():
    return accounts[0].deploy(DateTime)
