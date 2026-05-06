*** Settings ***
Library           AppiumLibrary

Suite Setup       Open App
Suite Teardown    Close App

*** Variables ***
${REMOTE_URL}       http://localhost:4723/wd/hub
${PLATFORM}         Android
${APP_PACKAGE}      com.example.avjindersinghsekhon.minimaltodo
${APP_ACTIVITY}     .Main.MainActivity
${APP_PATH}         ${CURDIR}/MinimalTodo.apk

*** Keywords ***
Open App
    Open Application    ${REMOTE_URL}
    ...    platformName=${PLATFORM}
    ...    appPackage=${APP_PACKAGE}
    ...    appActivity=${APP_ACTIVITY}
    ...    app=${APP_PATH}
    ...    automationName=UiAutomator2

Close App
    Close Application

Add Todo
    [Arguments]    ${text}
    Click Element    xpath=//android.widget.ImageButton[@content-desc="Add"]
    Input Text       xpath=//android.widget.EditText    ${text}
    Click Element    xpath=//android.widget.ImageButton[@content-desc="Done"]

*** Test Cases ***

TC01 Add todo item
    Add Todo    Buy groceries
    Element Should Be Visible    xpath=//android.widget.TextView[@text="Buy groceries"]

TC02 Add multiple todo items
    Add Todo    Go to gym
    Add Todo    Read a book
    Element Should Be Visible    xpath=//android.widget.TextView[@text="Go to gym"]
    Element Should Be Visible    xpath=//android.widget.TextView[@text="Read a book"]

TC03 Delete todo item
    Add Todo    Task to delete
    Swipe    500    500    100    500    500
    Element Should Not Be Visible    xpath=//android.widget.TextView[@text="Task to delete"]

TC04 Empty list on fresh start
    Element Should Be Visible    xpath=//android.widget.TextView[@text="Add a To-Do"]

TC05 Enable night mode
    Click Element    xpath=//android.widget.ImageView[@content-desc="More options"]
    Click Element    xpath=//android.widget.TextView[@text="Night Mode"]
    Element Should Be Visible    xpath=//android.widget.TextView[@text="Night Mode"]
