# Created by saged at 2/28/2023

Feature: Amazon main page tests

  Scenario: User can see hamburger menu
    Given Open Amazon page
    Then Verify hamburger menu icon present

  Scenario: Footer and header has correct number of links
    Given Open amazon page
    Then Verify that footer has 42 links
    Then Verify that header has 29 links