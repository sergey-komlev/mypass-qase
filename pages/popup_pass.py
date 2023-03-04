from playwright.sync_api import Page
import config


class PopupPass:
    _INPUT_NUMBER = "//input[@placeholder='Номер телефона или имя']"
    _OPTION_PROFILE = "//span[contains(text(), 'Каспер Сергей')]"
    # _ERROR_MESSAGE = "//span[contains(text(), 'Введены не все данные: Организация')]"
    _BUTTON_CREATE_PASS = "//div[@class='modalFooter']//button[contains(text(), 'Создать пропуск')]"

    def enter_number(self, page: Page, phone_number):
        page.locator(self._INPUT_NUMBER).fill(phone_number)

    def select_profile(self, page: Page):
        page.locator(self._OPTION_PROFILE).click()

    def press_button_create_pass(self, page: Page):
        page.locator(self._BUTTON_CREATE_PASS).click()

    @staticmethod
    def check_error_message(page: Page, expected_text) -> None:
        page.get_by_text(expected_text)
