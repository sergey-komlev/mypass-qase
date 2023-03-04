from playwright.sync_api import Page
import config


class AuthPage:
    _INPUT_NUMBER = "//input[@placeholder='( _ _ _ ) _ _ _  _ _ _ _']"
    _BUTTON_VOUTI = "//button[contains(text(), 'Войти')]"
    _TEXT_CODE = "//span[contains(text(), 'Ваш код:')]"
    _INPUT_CODE = "//input[@maxlength='5']"

    def open_auth_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def enter_number(self, page: Page, phone):
        page.locator(self._INPUT_NUMBER).fill(phone)

    def press_vouti_button(self, page: Page):
        page.locator(self._BUTTON_VOUTI).click()

    def get_code(self, page: Page):
        return page.locator(self._TEXT_CODE).text_content()[9:]

    def enter_code(self, page: Page, value):
        page.locator(self._INPUT_CODE).fill(value)
