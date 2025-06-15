from playwright.sync_api import expect, Page
import pytest


# В задании указан "Пример параметризованного автотеста", что читается не как жесткое требование.

# Сменил язык name на английский для вывода в консоль
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
def test_wrong_email_or_password_authorization(case, chromium_page: Page):

    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    email_input = chromium_page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input.fill(case["email"])

    password_input = chromium_page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input.fill(case["password"])

    login_button = chromium_page.locator('//button[@data-testid="login-page-login-button"]')
    login_button.click()

    wrong_email_or_password_alert = chromium_page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]') 
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")