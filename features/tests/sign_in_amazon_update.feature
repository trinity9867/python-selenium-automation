# Created by saged at 2/19/2023
Feature: Logged out Sign in verification


  Scenario: User can see sign in page after logging out
    Given Open Amazon page
    When  Click on Returns and Orders
    Then  Verify Sign in page is visible