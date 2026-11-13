*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  valid_username
    Set Password  valid_password
    Set Confirmation Password  valid_password
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Numbers
    Set Username  valid_username
    Set Password  kalle123
    Set Confirmation Password  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Special Characters
    Set Username  valid_username
    Set Password  kalle#abc
    Set Confirmation Password  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Matching Password Confirmation
    Set Username  valid_username
    Set Password  kalle123
    Set Confirmation Password  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Non-Matching Password Confirmation
    Set Username  valid_username
    Set Password  kalle123
    Set Confirmation Password  kalle456
    Click  button >> text=Register
    Register Should Fail With Message  Password confirmation doesn't match

Register With Password Containing Only Lowercase Letters
    Set Username  valid_username
    Set Password  kallekalle
    Set Confirmation Password  kallekalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Password Containing Only Uppercase And Lowercase Letters
    Set Username  valid_username
    Set Password  KalleKalle
    Set Confirmation Password  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Too Short Username And Valid Password
    Set Username  xx
    Set Password  valid_password
    Set Confirmation Password  valid_password
    Click  button >> text=Register
    Register Should Fail With Message  Username must contain at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  valid_username
    Set Password  pswrd
    Set Confirmation Password  pswrd
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain at least 8 characters

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  valid_password
    Set Confirmation Password  valid_password
    Click  button >> text=Register
    Register Should Fail With Message  Username already in use

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}
    Register Page Should Be Open

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page