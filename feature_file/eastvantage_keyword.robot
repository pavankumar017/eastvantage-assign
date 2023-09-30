***Keywords***

Open Browser "${URL}"
    utils.open_browser  ${URL}

Close Browser
    utils.close_browser

User Clicks on login
    test.click_login

User enters emailid
    test.enter_username

User enters password
    test.enter_pwd

User clicks on login in authentication screen
    test.click_login_auth_screen

User is logged in
    test.verify_login

User clicks on submit application
    test.click_submit_application
    
User scrolls down and clicks on submit new application
    test.click_submit_new_application

User Enters All the mandatory fields with firstname as "${firstname}"
    test.enter_first_name  ${firstname}
    test.enter_last_name
    test.enter_address
    test.enter_postcode
    test.select_country_india
    test.upload_image
    test.select_gender
    test.select_role
    test.select_tools
    test.enter_career_objective
    test.click_next

User should verify the deatils entered in summary page
    test.verify_summary_details