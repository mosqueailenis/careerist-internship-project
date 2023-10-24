Feature: User sign in and edit personal information

  Scenario: User can go to settings and edit the personal information
    Given Open the main page mobile web
    And Log in to the page mobile web
    When Click on settings option mobile web
    And Click on Edit profile option mobile web
    And Enter some test information in the input fields mobile web
    Then Check the right information is present in the input fields mobile web
    And Check the "Close" and "Save Changes" buttons clickable mobile web