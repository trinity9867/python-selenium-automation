# Created by saged at 2/24/2023
Feature: Shopping cart test


  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Input text lifewater
    When Click on search button
    And Click on the first product
    And Click on Add to Cart button
    And Open Cart page
    Then Verify that cart has 1 item


