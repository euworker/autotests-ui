from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

     # Проверяем, что кнопка registration не активна
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

     # фокусируемся и вводим текст в поле email
    registration_form_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_form_email_input.focus()
    registration_form_email_input.type("user.name@gmail.com", delay=150)

     # фокусируемся и вводим текст в поле user
    registration_form_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_form_username_input.focus()
    registration_form_username_input.type("username", delay=150)

     # фокусируемся и вводим текст в поле password
    registration_form_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_form_password_input.focus()
    registration_form_password_input.type("password", delay=150)

     # Проверяем, что кнопка registration активна
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_enabled()


