# from playwright.sync_api import expect, Page
import pytest
from pages.login_page import LoginPage

logins_pass_list =[ {
    "name": "user cannot log in with invalid email and password",
    "email": "user.name@gmail.com",
    "password": "password"
},
{
    "name": "user cannot log in with an invalid email and an empty password",
    "email": "user.name@gmail.com",
    "password": "  "
},
{
    "name": "user cannot log in with an empty email and invalid password",
    "email": "  ",
    "password": "password"
}
]

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("case", logins_pass_list, ids=lambda test_case: f"{test_case['name']} ({test_case['email']})")
def test_wrong_email_or_password_authorization(login_page: LoginPage, case):

    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.fill_login_form(email=case["email"], password=case["password"])
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()

    # chromium_page: Page

    