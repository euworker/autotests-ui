import pytest

@pytest.fixture
def clear_books_database() -> None:
    print("[FIXTURE] Удаляем все данные из бызы")

@pytest.fixture
def fill_books_database() -> None:
    print("[FIXTURE] Создаем новые данные в базе")

@pytest.mark.usefixtures('clear_books_database')
def test_read_all_books_in_labrary():
    print("Reading all books")     

#фиксуры запускаются по очереди
@pytest.mark.usefixtures(
    'clear_books_database',
    'fill_books_database'
    )
class TestLibrary:
    def test_read_book_from_library(self):
        print("Reading all books")    

    def test_delete_all_books_form_library(self):
        print("Delete all books")