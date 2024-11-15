Feature: SignUp

  Scenario: Create a new account
    Given I am on the homepage and I click on the SignUp button
    When the SignUp field is displayed
    And I enter 'mirceaun' as the name of the new user and the random generated email is entered and the SignUp button is pressed
    When the account information field becomes visible
    And I enter 'mircea' as username and '123abc' as password and I set '7' 'March' '1989' as birthday to fill the account information
    When I enter that I am 'Mircea' 'Ungureanu' from 'Company' living at 'Corner' 'Street' in Singapore, 'Ro', 'Bucharest', zip '06074' with phone '0740560980'
    And I press the create account button
    When I receive the message that the account has been created and I continue
    Then I arrive on my account page, I delete my account and I get a confirmation message that the account has been deleted

