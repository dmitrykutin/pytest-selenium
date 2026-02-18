from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "http://localhost:8000/index.html"

    def __init__(self, driver):
        super().__init__(driver)
        self.MODAL_OPEN_BTN = ("id", "open-modal")
