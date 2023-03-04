import pytest
import pages
from tests.base_test import BaseTest
import time


class TestAuthPage(BaseTest):

    def test_user_should_be_able_to_sing_in(self, page, user):
        self.user_sing_in(page, user.PHONE_NUMBER)
        time.sleep(10)
