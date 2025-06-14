from playwright.sync_api import expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):

    #   Забрать страницу из фикстуры
    page = chromium_page_with_state

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
