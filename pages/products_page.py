import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductsPage(BasePage):
    PRODUCTS_BUTTON = (By.PARTIAL_LINK_TEXT, 'Products')
    ALL_PRODUCTS_LIST = (By.XPATH, "//div[@class='features_items']//descendant::div[@class='col-sm-4']")
    FIRST_PRODUCT = (By.XPATH, "//div[@class='features_items']//descendant::div[@class='col-sm-4'][1]//descendant::a[@href='/product_details/1']")
    FIRST_PRODUCT_NAME = (By.XPATH, "//div[@class='product-information']//following-sibling::h2")
    FIRST_PRODUCT_CATEGORY = (By.XPATH, "//div[@class='product-information']//following-sibling::p")
    FIRST_PRODUCT_PRICE = (By.XPATH, "//div[@class='product-information']//following-sibling::span[contains(text(),'500')]")
    FIRST_PRODUCT_AVAILABILITY = (By.XPATH, "//div[@class='product-information']//following-sibling::p[contains(text(),'Stock')]")
    FIRST_PRODUCT_CONDITION = (By.XPATH, "//div[@class='product-information']//following-sibling::p[contains(text(),'New')]")
    FIRST_PRODUCT_BRAND = (By.XPATH, "//div[@class='product-information']//following-sibling::p[contains(text(),'Polo')]")
    HOMEPAGE_PRODUCTS_CATEGORY = (By.CSS_SELECTOR, "div[class='left-sidebar']")
    HOMEPAGE_PRODUCTS_BRANDS = (By.CSS_SELECTOR, "div[class='brands_products']")
    CATEGORY_WOMAN_PRODUCTS = (By.CSS_SELECTOR, "a[href='#Women']")
    PRODUCTS_WOMAN_DRESS = (By.CSS_SELECTOR, "a[href='/category_products/1']")
    TITLE_PRODUCTS_WOMAN_PAGE = (By.CSS_SELECTOR, "h2[class='title text-center']")
    CATEGORY_MAN_PRODUCTS = (By.CSS_SELECTOR, "a[href='#Men']")
    PRODUCTS_MAN_JEANS = (By.CSS_SELECTOR, "a[href='/category_products/6']")



    def open_products(self):
        self.open_homepage()
        assert self.verify_current_url('https://automationexercise.com/')
        self.click(self.PRODUCTS_BUTTON)

    def products_page_title(self):
        assert self.verify_current_page_title('Automation Exercise - All Products')

    def products_are_visible(self):
        assert len(self.find_all(self.ALL_PRODUCTS_LIST)) > 0
        self.driver.implicitly_wait(10)

    def product_details(self):
        element = self.find(self.FIRST_PRODUCT)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        self.click(self.FIRST_PRODUCT)
        assert self.verify_current_url('https://automationexercise.com/product_details/1')
        assert self.verify_if_is_displayed(self.FIRST_PRODUCT_NAME)
        assert self.verify_if_is_displayed(self.FIRST_PRODUCT_CATEGORY)
        assert self.verify_if_is_displayed(self.FIRST_PRODUCT_PRICE)
        assert self.verify_if_is_displayed(self.FIRST_PRODUCT_AVAILABILITY)
        assert self.verify_if_is_displayed(self.FIRST_PRODUCT_CONDITION)
        assert self.verify_if_is_displayed(self.FIRST_PRODUCT_BRAND)

    def homepage_products_categories_visible(self):
        self.driver.implicitly_wait(10)
        self.open_homepage()
        assert self.verify_current_url('https://automationexercise.com/')
        assert self.verify_if_is_displayed(self.HOMEPAGE_PRODUCTS_CATEGORY)
        assert self.verify_if_is_displayed(self.HOMEPAGE_PRODUCTS_BRANDS)

    def click_category_woman_dress(self):
        self.driver.implicitly_wait(10)
        self.click(self.CATEGORY_WOMAN_PRODUCTS)
        self.click(self.PRODUCTS_WOMAN_DRESS)

    def dress_products_visible(self):
        self.driver.implicitly_wait(10)
        assert self.verify_current_page_title('Automation Exercise - Dress Products')
        assert self.verify_current_url('https://automationexercise.com/category_products/1')
        #assert self.text_selector(self.TITLE_PRODUCTS_WOMAN_PAGE) == "WOMEN - DRESS PRODUCTS"

    def click_category_man_jeans(self):
        self.click(self.CATEGORY_MAN_PRODUCTS)
        self.click(self.PRODUCTS_MAN_JEANS)

    def jeans_products_visible(self):
        assert self.verify_current_page_title('Automation Exercise - Jeans Products')
