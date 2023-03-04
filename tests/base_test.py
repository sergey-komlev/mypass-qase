import pages


class BaseTest:
    def user_sing_in(self, page, phone_number):
        pages.auth_page.open_auth_page(page)
        pages.auth_page.enter_number(page, phone_number)
        pages.auth_page.press_vouti_button(page)
        code = pages.auth_page.get_code(page)
        pages.auth_page.enter_code(page, code)
