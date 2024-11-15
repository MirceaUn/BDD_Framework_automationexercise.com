from selenium import webdriver


class Browser:

    def __init__(self):
        self.driver = None

    def get_driver(self):
        if self.driver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
        return self.driver

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
