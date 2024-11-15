Feature: Products

  Scenario: Verify All Products and product detail page
    Given that I am on the homepage and I click on the Products button
    When the page changes I can see that I am on the ALL PRODUCTS page
    And the products list is visible
    Then I click on the first product and on the product page I can see details like Name, Category, Price, Availability, Condition, Brand


  Scenario: View Category Products
    Given that I am on the homepage I look on the left side to see the Category and Brands fields
    When I click on Woman category and I click on the category of dresses
    And I am taken to the dedicated page of Woman Dresses
    And if I click on Man category and I click on the category of jeans
    Then I will be taken to the dedicated page of Man Jeans