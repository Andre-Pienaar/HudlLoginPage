Hudl Login Tests
    This is a set of automated tests to verify the login functionality of the Hudl website.

Prerequisites
    Python 3.x 
    Pip 
    Chrome web browser


Installation
    Clone this repository to your local machine.
    Open a terminal and navigate to the project directory.
    Install the required dependencies with the following command:
        pip install -r requirements.txt


Usage
    To run all the tests, execute the following command:
        pytest LoginPageTests.py

    To run a specific test, execute the following command:
        pytest -k test_method_name LoginPageTests.py
    Replace "test_method_name" with the name of the test method you want to run.

Description of the tests:
    test_successfully_login - This test logs in with a valid email and password and verifies that the search input is displayed on the home page.
    test_fail_login_without_input - This test attempts to login without entering any credentials and verifies that an error message is displayed.
    test_fail_login_with_wrong_email - This test attempts to login with an invalid email and verifies that an error message is displayed.
    test_fail_login_with_wrong_password - This test attempts to login with an invalid password and verifies that an error message is displayed.
    test_need_help_link - This test clicks the "Need Help?" link on the login page and verifies that the login help page is displayed.
    test_signup_link - This test clicks the "Sign up" link on the login page and verifies that the registration page is displayed.

Fixtures
    browser_setup_and_teardown - This fixture sets up the Chrome webdriver and opens the Hudl website. After each test, it closes the browser. This fixture is applied to all the tests using the autouse=True argument.

Structure
    PageObject/ - This directory contains the page object classes used in the tests.
    LoginPageTests.py This file contains all the tests
    requirements.txt - This file lists all the packages required to run the tests.
    README.md - This file.