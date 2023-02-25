# Created by saged at 2/21/2023
Feature: Amazon Best Sellers page


  Scenario: User can open Amazon Best Sellers page
    Given Open Amazon page
    When  Click on Best Sellers
    Then  Verify that 5 links are shown


