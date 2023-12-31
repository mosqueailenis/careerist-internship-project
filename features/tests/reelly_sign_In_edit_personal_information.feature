
Feature: User sign in and edit personal information

  Scenario: User can go to settings and edit the personal information
    Given Open the main page
    And Log in to the page
    When Click on settings option
    And Click on Edit profile option
    And Enter some test information in the input fields
    Then Check the right information is present in the input fields
    And Check the "Close" and "Save Changes" buttons clickable

