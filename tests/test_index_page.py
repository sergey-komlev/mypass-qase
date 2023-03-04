import pytest
import pages
import time


class TestFooter:

    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.enter_number_input(page)
        time.sleep(10)
