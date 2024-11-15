import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser import Browser


class BasePage(Browser):

    TERMS_CONDITIONS = (By.CSS_SELECTOR, 'button[aria-label="Consent"]')

    def __init__(self, webdriver):
        self.driver = webdriver

    def open_homepage(self):
        self.driver.get('https://automationexercise.com/')
        self.click(self.TERMS_CONDITIONS)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def type(self, locator, text):
        return self.find(locator).send_keys(text)

    def text_selector(self,locator):
        return self.find(locator).text

    def click(self, locator):
        return self.find(locator).click()

    def verify_if_is_displayed(self, locator):
        return self.find(locator).is_displayed()

    def verify_current_url(self, expected_url):
        return self.driver.current_url == expected_url

    def verify_current_page_title(self, expected_title):
        return self.driver.title == expected_title

    def verify_if_is_enabled(self, locator):
        return self.find(locator).is_enabled()

    def select_dropdown_item_by_text(self, locator, text):
        dropdown = Select(self.find(locator))
        dropdown.select_by_visible_text(text)

    def generate_email(self):
        random_email = f"mircea{random.randint(99999, 9999999999999)}@gmail.ro"
        return random_email



