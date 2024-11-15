from browser import Browser
from pages.products_page import ProductsPage
from pages.signup_page import SignUpPage
from pages.login_page import LoginPage


def before_scenario(context, scenario):
    context.driver = Browser().get_driver()
    context.signup_page = SignUpPage(context.driver)
    context.login_page = LoginPage(context.driver)
    context.products_page = ProductsPage(context.driver)


def after_scenario(context, scenario):
    context.signup_page.close_browser()
