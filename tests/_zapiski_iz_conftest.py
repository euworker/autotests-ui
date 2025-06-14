# ЭТО ОСТАВЛЯЮ ДЛЯ СЕБЯ

# @pytest.fixture
# # чказываем игонрирование типа, чтобы избежать ошибки в Page
# def chromium_page() -> Page: # type: ignore
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)        
#         yield browser.new_page()
#         browser.close()


# есть вероятность, что нужно сделать так 
# from typing import Generator
# from playwright.sync_api import sync_playwright, Page
# import pytest

# @pytest.fixture
# def chromium_page() -> Generator[Page, None, None]:  # Здесь используем правильный тип Generator
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         page = browser.new_page()
#         yield page   # Возвращаем страницу
#         browser.close()