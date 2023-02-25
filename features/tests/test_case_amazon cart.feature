# Created by saged at 2/18/2023

Feature:  Test Scenarios for Amazon shopping cart


  Scenario: User can verify shopping cart is empty
    Given Open Amazon page
    When  Click on Cart icon
    Then  Verify that Cart is empty
