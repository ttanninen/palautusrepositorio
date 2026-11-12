*** Settings ***
Library  Browser
Library  ../AppLibrary.py

*** Variables ***
${SERVER}        localhost:5001
${DELAY}         500ms
${HOME_URL}      http://${SERVER}
${LOGIN_URL}     http://${SERVER}/login
${REGISTER_URL}  http://${SERVER}/register
${BROWSER}       chromium
${HEADLESS}      false

*** Keywords ***
Open And Configure Browser
    IF  $HEADLESS == 'true'
        New Browser  browser=${BROWSER}  headless=True
    ELSE
        New Browser  browser=${BROWSER}  headless=False  slowMo=${DELAY}
    END
    New Context
    New Page  about:blank

Login Page Should Be Open
    Get Title  ==  Login

Register Page Should Be Open
    Get Title  ==  Register

Main Page Should Be Open
    Get Title  ==  Ohtu Application main page

Welcome Page Should Be Open
    Get Title  ==  Welcome to Ohtu Application!

Go To Login Page
    Go To  ${LOGIN_URL}

Go To Register Page
    Go To  ${REGISTER_URL}

Go To Starting Page
    Go To  ${HOME_URL}

Set Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Set Password
    [Arguments]  ${password}
    Fill Secret  id=password  $password

Set Confirmation Password
    [Arguments]  ${password_confirmation}
    Fill Secret  id=password_confirmation  $password_confirmation