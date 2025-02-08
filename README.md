About the project

The test cases from this repository have been developed using the POM Design Pattern and the BDD Framework.
The website where the tests were conducted is: https://automationexercise.com/

They were built in Python using:
- Selenium Module
- Behave Module
- Unittest Library
- Cucumber Plugin
- Gherkin Plugin
- Ini Plugin

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tests description

- The SignUp Feature contains one Scenario: "Create a new account" which recounts all the steps needed to create a new account and, in the end, deletes the newly created account
- The Login Feature contains 2 Scenarios:
    - Signing In with the correct credentials: asserts that I am logged in and the URL changed
    - Signing In with the wrong credentials (in one case with the wrong username and the other with the wrong password): asserts that an error message is displayed
- The Products Feature contains 2 Scenarios:
    - Verify All Products Page and Product Detail page: asserts that I can enter and view the products from All Products Page and, once clicked on one of the products, I am taken to that Products' page   
    - View Category Product: asserts that I can correctly interact with the Category buttons displayed on the left part of the page
