About the project - The scope of this suite is to test some of the functionalities of various pages from the website: https://automationexercise.com/

Prerequisites

PyCharm 2024.3.2

The Python code for these tests was written using PyCharm 2024.3.2. The version of Python can be checked in cmd.exe using the command: "python --version". In my case, it is Python 3.12.

Selenium Module 4.28.1

Used to automate web browser interaction from Python

Behave Module 1.2.7.dev6 & Cucumber 17.10.0 & Gherkin 243.22562.13 

Tools used for creating the BDD Framework (Behaviour driven development) in Python

Behave-html-formatter 0.9.10 & Ini 243.23654.177

Made for the Behave Module in order to create HTML reports of the tests conducted

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tests description

- The SignUp Feature contains one Scenario: "Create a new account" which recounts all the steps needed to create a new account and, in the end, deletes the newly created account
- The Login Feature contains 2 Scenarios:
    - Signing In with the correct credentials: asserts that I am logged in and the URL changed
    - Signing In with the wrong credentials (in one case with the wrong username and the other with the wrong password): asserts that an error message is displayed
- The Products Feature contains 2 Scenarios:
    - Verify All Products Page and Product Detail page: asserts that I can enter and view the products from All Products Page and, once clicked on one of the products, I am taken to that Products' page   
    - View Category Product: asserts that I can correctly interact with the Category buttons displayed on the left part of the page
