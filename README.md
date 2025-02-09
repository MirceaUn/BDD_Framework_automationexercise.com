About the project - The scope of this suite is to test some of the functionalities of various pages from the website: https://automationexercise.com/

Prerequisites

    1. PyCharm 2024.3.2

The Python code for these tests was written using PyCharm 2024.3.2. The version of Python can be checked in cmd.exe using the command: "python --version". In my case, it is Python 3.12.

    2. Selenium Module 4.28.1

Used to automate web browser interaction from Python

    3. Behave Module 1.2.7.dev6 & Cucumber 17.10.0 & Gherkin 243.22562.13 

Tools used for creating the BDD Framework (Behaviour driven development) in Python

    4. Behave-html-formatter 0.9.10 & Ini 243.23654.177

Made in order to create HTML reports of the tests conducted

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Installation and setup

1. A folder needs to be created in the computer, where the code to run the app will be stored
2. A new project needs to be opened in PyCharm and a virtual environment needs to be created 
3. The structure of a project using the BDD framework is the following:
   - The folder "features" contains the feature files for each page where we conduct tests. These files contain the steps of each text written in a simple language that everyone can understand 
   - The folder "pages" contains the Python files, with the written code for each test, for each page where we will conduct tests
   - The folder "steps" contains the files where we make the binding between the coded test and the text used to describe, in a simple language that everyone can understand, the steps of the tests
   - The file "Browser" contains the needed steps to open the browser and close the browser
   - The file "Environment" defines the setup (the steps prior to the actual test) and teardown (all the steps needed after running the test) functions  

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tests description

- The SignUp Feature contains one Scenario: "Create a new account" which recounts all the steps needed to create a new account and, in the end, deletes the newly created account
  
- The Login Feature contains 2 Scenarios:
    - Signing In with the correct credentials: asserts that I am logged in and the URL changed
    - Signing In with the wrong credentials (in one case with the wrong username and the other with the wrong password): asserts that an error message is displayed
      
- The Products Feature contains 2 Scenarios:
    - Verify All Products Page and Product Detail page: asserts that I can enter and view the products from All Products Page and, once clicked on one of the products, I am taken to that Products' page   
    - View Category Product: asserts that I can correctly interact with the Category buttons displayed on the left part of the page

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Running the tests

In the PyCharm terminal we use the following command line:

    behave -f=html "-o=raport.html"

And all the tests will go live and after that the results will be shown in the newly generated HTML report (raport.html in our example).
In case we add decorators (filters) on tests and we want to run only the filtered tests we have to explicit this in the command line from above.

