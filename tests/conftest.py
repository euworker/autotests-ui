import pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture() 
def chromium_page(playwright: Playwright) -> Page: # type: ignore
    browser = playwright.chromium.launch(headless=False)        
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):

    #   Создать новый браузер
    browser = playwright.chromium.launch(headless=False)
    #   Создать контекст в бразуере
    context = browser.new_context()
    #   Создать страницу в новом контексте
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


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page: # type: ignore
    #   из initialize_browser_state мы забираем только context, но не браузер
    #   Создать браузер и новый контекст с сохраненным состоянием 
    browser = playwright.chromium.launch(headless=False)
    #   Использовать сохраненное состояние
    context = browser.new_context(storage_state="browser-state.json") 
    #   Создать страницу в новом контексте
    page = context.new_page() 
    #   Возвратить страницу для использования в тестах
    yield page  
    #   Закрыть браузер
    browser.close()  