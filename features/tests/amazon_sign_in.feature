# Created by saged at 3/7/2023
Feature: Amazon sign in tests
  # Enter feature description here

  Scenario: Sign in page can be opened from sign in popup
    Given Open Amazon page
    When CLick sign in form popup
    Then Verify Sign in page opens

   Scenario: Sign in popup is visible for a few seconds
     Given Open Amazon page
     When Wait for 8 sec
     Then Verify sign in popup disappears
