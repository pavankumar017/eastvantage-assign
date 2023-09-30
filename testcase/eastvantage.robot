**Settings***
Library  SeleniumLibrary
Library  /Users/pavankumar/VSCODE/eastvantage-assign/src/test.py
Library  /Users/pavankumar/VSCODE/eastvantage-assign/src/utils.py


Resource  /Users/pavankumar/VSCODE/eastvantage-assign/feature_file/eastvantage_keyword.robot


Suite Setup  Open Browser "https://automationinterface1.front.staging.optimy.net/en/"
# Suite Teardown  Close Browser

*** Test Cases ***
User to verify login functionality 
    Given User Clicks on login
    And User enters emailid 
    And User enters password
    Then User clicks on login in authentication screen

User to test submitting a application
    Given User is logged in
    And User clicks on submit application
    And User scrolls down and clicks on submit new application
    And User Enters All the mandatory fields with firstname as "Test"
    Then User should verify the deatils entered in summary page


