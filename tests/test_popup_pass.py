import pytest
import pages
from tests.base_test import BaseTest
import time


class TestPopupPass(BaseTest):

    def test_user_should_be_able_to_see_error_message_about_unfilled_organization(self, page, user):
        self.user_sing_in(page, user.PHONE_NUMBER)
        pages.menu.press_create_pass_button(page)
        pages.popup_pass.enter_number(page, user.PHONE_NUMBER)
        pages.popup_pass.select_profile(page)
        pages.popup_pass.press_button_create_pass(page)
        pages.popup_pass.check_error_message(page, 'Введены не все данные: Организация')
