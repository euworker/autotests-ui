from playwright.sync_api import sync_playwright, expect

def test_successful_registration():

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        # Откроет страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration +
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Заполнит поле "Email" значением "user.name@gmail.com" +
        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        registration_email_input.fill("user.name@gmail.com")

        # Заполнит поле "Username" значением "username" +
        registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        registration_username_input.fill("username")

        # Заполнит поле "Password" значением "password" +
        registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        registration_password_input.fill("password")
        
        # Нажмет на кнопку "Registration". После нажатия кнопки "Registration" произойдет редирект на страницу "Dashboard"
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # не совсем уверен в этом блоке -> по идее, нужно  уточнить,куда мы попадаем, в мануальном тесте это вроде как указано - произойдет редирект на страницу "Dashboard"
        expected_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'
        page.wait_for_url(expected_url)

        # Проверит, что на странице "Dashboard" отображается заголовок "Dashboard"
        dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")
        expect(dashboard_title).to_be_visible()
        expect(dashboard_title).to_have_text("Dashboard")