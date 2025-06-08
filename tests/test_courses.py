from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        #   Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        
        #   Заполнить форму регистрации и нажать на кнопку "Registration"
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()


        #   Сохранить состояние браузера 
        context.storage_state(path="browser-state.json")

        #   Создать новую сессию браузера. В контекст необходимо подставить сохраненное состояние
        context = browser.new_context(storage_state="browser-state.json")


        #   Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses. Страница "Courses" должна открыться без авторизации
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")


        #   Доп шаг проверки url
        expected_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
        page.wait_for_url(expected_url)


        #   Проверить наличие и текст заголовка "Courses"
        courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text("Courses")


        #   Проверить иконку
        empty_icon = page.get_by_test_id("courses-list-empty-view-icon")
        expect(empty_icon).to_be_visible()

        #   Проверить наличие и текст блока "There is no results"
        empty_title = page.get_by_test_id("courses-list-empty-view-title-text")
        expect(empty_title).to_be_visible()
        expect(empty_title).to_have_text("There is no results")


        #   Проверить наличие и текст блока "Description"
        empty_description_text = page.get_by_test_id("courses-list-empty-view-description-text")
        expect(empty_description_text).to_be_visible()
        expect(empty_description_text).to_have_text("Results from the load test pipeline will be displayed here")
