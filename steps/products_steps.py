from behave import *

@given("that I am on the homepage and I click on the Products button")
def step_impl(context):
    context.products_page.open_products()

@when("the page changes I can see that I am on the ALL PRODUCTS page")
def step_impl(context):
    context.products_page.products_page_title()

@when("the products list is visible")
def step_impl(context):
    context.products_page.products_are_visible()

@then("I click on the first product and on the product page I can see details like Name, Category, Price, Availability, Condition, Brand")
def step_impl(context):
    context.products_page.product_details()

@given("that I am on the homepage I look on the left side to see the Category and Brands fields")
def step_impl(context):
    context.products_page.homepage_products_categories_visible()

@when("I click on Woman category and I click on the category of dresses")
def step_impl(context):
    context.products_page.click_category_woman_dress()

@when("I am taken to the dedicated page of Woman Dresses")
def step_impl(context):
    context.products_page.dress_products_visible()

@when("if I click on Man category and I click on the category of jeans")
def step_impl(context):
    context.products_page.click_category_man_jeans()

@then("I will be taken to the dedicated page of Man Jeans")
def step_impl(context):
    context.products_page.jeans_products_visible()