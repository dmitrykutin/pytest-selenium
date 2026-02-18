from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "http://localhost:8000/index.html"

    def __init__(self, driver):
        super().__init__(driver)
        self.MODAL_OPEN_BTN = ("id", "open-modal")
        self.MODAL_CLOSE_BTN = ("id", "close-modal")

    def open_modal(self):
        self.click(self.MODAL_OPEN_BTN)

    def close_modal(self):
        self.click(self.MODAL_CLOSE_BTN)

    def is_modal_visible(self):
        return "hidden" not in self.driver.find_element(
            *self.MODAL_OPEN_BTN
        ).get_attribute("class")
