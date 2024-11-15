import unittest
from selenium.webdriver.common.by import By


from pages.base_page import BasePage


class SignUpPage(BasePage, unittest.TestCase):
    SIGNUP_BUTTON = (By.PARTIAL_LINK_TEXT, 'Signup')
    NEW_USER_SIGNUP = (By.CLASS_NAME, 'signup-form')
    NAME_NEW_USER = (By.CSS_SELECTOR, 'input[placeholder="Name"]')
    EMAIL_NEW_USER = (By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
    CLICK_SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    ACCOUNT_INFORMATION_FIELD = (By.CLASS_NAME, 'login-form')
    TITLE_RADIO_BUTTON = (By.ID, 'id_gender1')
    NAME_FIELD = (By.ID, 'name')
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'password')
    DROPDOWN_DAY = (By.ID, 'days')
    DROPDOWN_MONTH = (By.ID, 'months')
    DROPDOWN_YEAR = (By.ID, 'years')
    NEWSLETTER_BUTTON = (By.ID, 'newsletter')
    OFFERS_BUTTON = (By.ID, 'optin')
    FIRST_NAME_FIELD = (By.ID, 'first_name')
    LAST_NAME_FIELD = (By.ID, 'last_name')
    COMPANY_FIELD = (By.ID, 'company')
    ADDRESS_1_FIELD = (By.ID, 'address1')
    ADDRESS_2_FIELD = (By.ID, 'address2')
    DROPDOWN_COUNTRY = (By.ID, 'country')
    STATE_FIELD = (By.ID, 'state')
    CITY_FIELD = (By.ID, 'city')
    ZIPCODE_FIELD = (By.ID, 'zipcode')
    MOBILE_NUMBER_FIELD = (By.ID, 'mobile_number')
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="create-account"]')
    ACCOUNT_CREATED_MESSAGE = (By.CSS_SELECTOR, 'h2[data-qa="account-created"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'a[data-qa="continue-button"]')
    DELETE_ACCOUNT_BUTTON = (By.LINK_TEXT, 'Delete Account')
    ACCOUNT_DELETED_MESSAGE = (By.CSS_SELECTOR, 'h2[data-qa="account-deleted"]')

    def open_sign_up(self):
        self.open_homepage()
        assert self.verify_current_url('https://automationexercise.com/')
        self.click(self.SIGNUP_BUTTON)

    def visibility_sign_up_field(self):
        assert self.verify_if_is_displayed(self.NEW_USER_SIGNUP)

    def fill_signup(self, name_new_user):
        self.type(self.NAME_NEW_USER, name_new_user)
        self.type(self.EMAIL_NEW_USER, self.generate_email())
        self.click(self.CLICK_SIGNUP_BUTTON)

    def account_information_visible(self):
        assert self.verify_if_is_displayed(self.ACCOUNT_INFORMATION_FIELD)
        self.driver.implicitly_wait(5)

    def fill_account_information(self, full_name, password, birth_day, birth_month, birth_year):
        self.click(self.TITLE_RADIO_BUTTON)
        self.type(self.NAME_FIELD, full_name)
        self.assertFalse(self.verify_if_is_enabled(self.EMAIL_FIELD))
        self.type(self.PASSWORD_FIELD, password)
        self.select_dropdown_item_by_text(self.DROPDOWN_DAY, birth_day)
        self.select_dropdown_item_by_text(self.DROPDOWN_MONTH, birth_month)
        self.select_dropdown_item_by_text(self.DROPDOWN_YEAR, birth_year)
        self.click(self.NEWSLETTER_BUTTON)
        element = self.find(self.OFFERS_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        self.click(self.OFFERS_BUTTON)

    def fill_address_info(self, first_name, last_name, company_name, address1, address2, state_name, city_name, zipcode,
                          mobile_number):
        self.driver.implicitly_wait(10)
        self.type(self.FIRST_NAME_FIELD, first_name)
        self.type(self.LAST_NAME_FIELD, last_name)
        self.type(self.COMPANY_FIELD, company_name)
        self.type(self.ADDRESS_1_FIELD, address1)
        self.type(self.ADDRESS_2_FIELD, address2)
        self.select_dropdown_item_by_text(self.DROPDOWN_COUNTRY, 'Singapore')
        self.type(self.STATE_FIELD, state_name)
        self.type(self.CITY_FIELD, city_name)
        self.type(self.ZIPCODE_FIELD, zipcode)
        self.type(self.MOBILE_NUMBER_FIELD, mobile_number)

    def create_account(self):
        self.driver.implicitly_wait(5)
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def visibility_created_account(self):
        self.driver.implicitly_wait(5)
        assert self.verify_if_is_displayed(self.ACCOUNT_CREATED_MESSAGE)
        self.click(self.CONTINUE_BUTTON)

    def delete_account(self):
        self.driver.implicitly_wait(5)
        self.click(self.DELETE_ACCOUNT_BUTTON)
        self.verify_if_is_displayed(self.ACCOUNT_DELETED_MESSAGE)
        self.click(self.CONTINUE_BUTTON)

    def close_browser(self):
        self.driver.implicitly_wait(5)
        self.close_driver()
