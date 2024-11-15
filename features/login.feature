Feature: Sign In


  Scenario: Sign In with correct credentials
    Given I am on the homepage and I click on the LogIn button
    When the Login to your account message is visible
    And I enter the username 'mircea.ungureanu@ymail.com' and the password 'mirc89' and I click the Login button
    Then the message "Logged in as Ungureanu Mircea" is visible


  Scenario Outline: Sign In with incorrect credentials
    Given I am on the homepage and I click on the LogIn button
    When the Login to your account message is visible
    And I enter the username '<username>' and the password '<password>' and I click the Login button
    Then the message "Your email or password is incorrect!" is visible
    Examples:
      | username                   | password |
      | m@23.ro                    | mirc89   |
      | mircea.ungureanu@ymail.com | m        |