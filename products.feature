Feature: Product management

  Scenario: Read a product
    Given the following products
      | name  | category   | price | available |
      | Phone | Electronics | 999   | True      |
    When I request the product by id 1
    Then the result should be the product "Phone"

  Scenario: Update a product
    Given the following products
      | name  | category   | price | available |
      | Phone | Electronics | 999   | True      |
    When I update the product with id 1 and set price to 1200
    Then the result should be a product with price "1200"

  Scenario: Delete a product
    Given the following products
      | name  | category   | price | available |
      | Phone | Electronics | 999   | True      |
    When I delete the product with id 1
    Then the product should no longer exist

  Scenario: List all products
    When I request the list of all products
    Then I should see a list of products

  Scenario: Search products by name
    When I search for products by name "Phone"
    Then the result should contain the product "Phone"
