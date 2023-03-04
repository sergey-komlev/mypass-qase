import pytest


class User:
    def __init__(self):
        self.PHONE_NUMBER = ''


@pytest.fixture()
def user():
    return User()
