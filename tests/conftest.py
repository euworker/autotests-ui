import pytest
from playwright.sync_api import Page, Playwright


# 6.5 Фикстуры Pytest Практика работы с pytest фикстурами (тесты на test_empty_courses_list)

#   Тестировал на test_empty_courses_list через $ python -m pytest -s -v -k test_empty_courses_list
#   Область видимости нужно будет изменять, если захочу передать chromium_page в initialize_browser_state по причине ошибок на разность области видимости фикстур, 
#   при этом Gigachat крайне рекомендует создавать отдельные фикстуры для браузера и страниц, 
#   что логично, ведь каждая тестовая функция получит свою уникальную страницу, независимо от общей сессии. Браузер останется открытым в течение всей сессии.
#   В данном задании не использовал chromium_page.
@pytest.fixture() 
def chromium_page(playwright: Playwright) -> Page: # type: ignore
        browser = playwright.chromium.launch(headless=False)        
        yield browser.new_page()
        browser.close()



# 6.5 Фикстуры Pytest Практика работы с pytest фикстурами (тесты на test_empty_courses_list)

#   @pytest.mark.usefixtures('chromium_page') - передача фикстуры в фикстуру таким способом вызывает ошибку deprecated. 
#   Предполагается, что такой способ и не должен был работать, судя по документации.
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

    #   Получить контекст страницы     
    context = page.context
    #   Сохранить состояние браузера 
    context.storage_state(path="browser-state.json")


# 6.5 Фикстуры Pytest Практика работы с pytest фикстурами (тесты на test_empty_courses_list)
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
    #   Закрыть контекст после завершения теста
    context.close()  
    #   Закрыть браузер
    browser.close()  