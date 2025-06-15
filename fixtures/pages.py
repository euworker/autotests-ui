import pytest
from playwright.sync_api import Page

from tests.pages.login_page import LoginPage
from tests.pages.registration_page import RegistrationPage
from tests.pages.dashboard_page import DashboardPage

# создаем фикстуру страницы логина импортируя в неё фикстуру chromium_page
@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)


@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)


@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page)