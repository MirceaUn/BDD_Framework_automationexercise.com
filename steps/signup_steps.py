from behave import *

@given("I am on the homepage and I click on the SignUp button")
def step_impl(context):
    context.signup_page.open_sign_up()

@when("the SignUp field is displayed")
def step_impl(context):
    context.signup_page.visibility_sign_up_field()

@when("I enter '{name_new_user}' as the name of the new user and the random generated email is entered and the SignUp button is pressed")
def step_impl(context, name_new_user):
    context.signup_page.fill_signup(name_new_user)

@when("the account information field becomes visible")
def step_impl(context):
    context.signup_page.account_information_visible()

@when("I enter '{full_name}' as username and '{password}' as password and I set '{birth_day}' '{birth_month}' '{birth_year}' as birthday to fill the account information")
def step_impl(context, full_name, password, birth_day, birth_month, birth_year):
    context.signup_page.fill_account_information(full_name, password, birth_day, birth_month, birth_year)

#I enter that I am Mircea Ungureanu from Company living at Corner Street in Singapore, Ro, Bucharest, zip 06074 with phone 0740560980
@when("I enter that I am '{first_name}' '{last_name}' from '{company_name}' living at '{address1}' '{address2}' in Singapore, '{state_name}', '{city_name}', zip '{zipcode}' with phone '{mobile_number}'")
def step_impl(context, first_name, last_name, company_name, address1, address2, state_name, city_name, zipcode, mobile_number):
    context.signup_page.fill_address_info(first_name, last_name, company_name, address1, address2, state_name, city_name, zipcode, mobile_number)

@when("I press the create account button")
def step_impl(context):
    context.signup_page.create_account()

@when("I receive the message that the account has been created and I continue")
def step_impl(context):
    context.signup_page.visibility_created_account()

@then("I arrive on my account page, I delete my account and I get a confirmation message that the account has been deleted")
def step_impl(context):
    context.signup_page.delete_account()