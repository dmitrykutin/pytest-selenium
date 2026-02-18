class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def goto(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.driver.find_element(*locator).click()
