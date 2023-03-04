from playwright.sync_api import Page


class Menu:
    _BUTTON_CREATE_PASS = "//button[contains(text(), 'Создать пропуск')]"

    def press_create_pass_button(self, page: Page) -> None:
        page.locator(self._BUTTON_CREATE_PASS).click()
