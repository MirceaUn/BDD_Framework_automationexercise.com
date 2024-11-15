from behave import *

@given("I am on the homepage and I click on the LogIn button")
def step_impl(context):
    context.login_page.open_login()

@when("the Login to your account message is visible")
def step_impl(context):
    context.login_page.login_message_displayed()

@when("I enter the username '{email}' and the password '{password}' and I click the Login button")
def step_impl(context, email, password):
    context.login_page.fill_login(email, password)

@then('the message "Logged in as Ungureanu Mircea" is visible')
def step_impl(context):
    context.login_page.logged_in_as_username_visible()

@then('the message "Your email or password is incorrect!" is visible')
def step_impl(context):
    context.login_page.login_error_message()