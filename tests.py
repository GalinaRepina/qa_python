import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет Вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_exceeds_length(self):
        collector = BooksCollector()
        collector.add_new_book('К' * 41)  # Книга с названием длиной 41 символ
        assert len(collector.get_books_genre()) == 0  # Не должно добавиться

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.set_book_genre("Книга 1", "Фантастика")
        assert collector.get_book_genre("Книга 1") == "Фантастика"

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 2", "Фантастика")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Книга 1", "Книга 2"]

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 2", "Ужасы")  # Жанр с возрастным рейтингом
        assert collector.get_books_for_children() == ["Книга 1"]  # Только "Книга 1" подходит детям

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.add_book_in_favorites("Книга 1")
        assert "Книга 1" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.add_book_in_favorites("Книга 1")
        collector.delete_book_from_favorites("Книга 1")
        assert "Книга 1" not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_twice(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.add_book_in_favorites("Книга 1")
        collector.add_book_in_favorites("Книга 1")  # Добавляем опять 
        assert collector.get_list_of_favorites_books().count("Книга 1") == 1  # Должно быть только одно

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.set_book_genre("Книга 1", "Фантастика")
        assert collector.get_books_genre() == {"Книга 1": "Фантастика"}
