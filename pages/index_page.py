from playwright.sync_api import Page
import config


class IndexPage:
    _INPUT_NUMBER = "//input[@class='si-input']"

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def enter_number_input(self, page: Page):
        page.locator(self._INPUT_NUMBER).fill("89067555567")
