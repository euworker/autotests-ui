import pytest

# в фикстурах в аргументах указываем различные параметры - например, autouse - будет всегда запускаться при любом тесте
# в фикстурах указываем скоуп применения - 
#   session (сессия - запустится 1 раз на весь запуск тестов, )
# scope="function" (по умолчанию): выполняется перед каждым тестом. Обычно используется для таких действий, как открытие браузера, создание какой-либо сущности, создание/удаление данных до/после автотеста. Самый часто используемый scope
# scope="module": выполняется один раз на уровне модуля. Файл = module. Очень редко используется
# scope="class": выполняется один раз для каждого класса с тестами. Используется для таких действий, как создание данных, которые нужны для всего тестового класса
# scope="package": выполняется один раз на уровне папки, внутри которой есть __init__.py файл. 
# scope="session": выполняется один раз за всю сессию тестирования. Используется для данных, которые нужны для всей тестовой сессии, например настройки автотестов


@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[autouse] Отправляем данные в сервис аналитики")

@pytest.fixture(scope="session")
def settings():
    print("[session] Инициализируем настройки автотестов")

@pytest.fixture(scope="class")
def user():
    print("[class] Созаем данные пользователя один раз на тестовый класс")

@pytest.fixture(scope="function")
def browser():
    print("[function] Открываем браузер на каждый автотест")




class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...

    def test_user_can_create_course(self, settings, user, browser):
        ...

class TestAccountFlow:
    def test_user_account(self):
        ...        