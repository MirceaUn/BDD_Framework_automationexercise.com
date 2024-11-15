from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    LOGIN_BUTTON = (By.PARTIAL_LINK_TEXT, 'Signup')
    LOGIN_ACCOUNT_MESSAGE = (By.XPATH, "//h2[contains(text(),'Login')]")
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGGED_IN_MESSAGE = (By.PARTIAL_LINK_TEXT, 'Logged')
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, "p[style='color: red;']")

    def open_login(self):
        self.open_homepage()
        assert self.verify_current_url('https://automationexercise.com/')
        self.click(self.LOGIN_BUTTON)

    def login_message_displayed(self):
        assert self.verify_if_is_displayed(self.LOGIN_ACCOUNT_MESSAGE)
        assert self.text_selector(self.LOGIN_ACCOUNT_MESSAGE) == 'Login to your account'

    def fill_login(self, email, password):
        self.type(self.LOGIN_EMAIL_FIELD, email)
        self.type(self.LOGIN_PASSWORD_FIELD, password)
        self.click(self.LOGIN_ACCOUNT_BUTTON)

    def login_error_message(self):
        assert self.verify_if_is_displayed(self.LOGIN_ERROR_MESSAGE)
        assert self.text_selector(self.LOGIN_ERROR_MESSAGE) == 'Your email or password is incorrect!'

    """
    username: mircea.ungureanu@ymail.com
    pass: mirc89
    """

    def logged_in_as_username_visible(self):
        assert self.verify_if_is_displayed(self.LOGGED_IN_MESSAGE)
        assert self.text_selector(self.LOGGED_IN_MESSAGE) == 'Logged in as Ungureanu Mircea'

    def close_browser(self):
        self.driver.implicitly_wait(5)
        self.close_driver()



