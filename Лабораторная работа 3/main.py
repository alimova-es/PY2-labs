class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        """Геттер не принимает никаких агрументов, но должен возвращать какой-то результат."""
        return self._name  # внутри класса обращаемся к защищенному атрибуту

    @property
    def author(self):
        """Геттер не принимает никаких агрументов, но должен возвращать какой-то результат."""
        return self._author  # внутри класса обращаемся к защищенному атрибуту

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    # используется метод pages и @property
    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    # используется метод pages и @pages.setter
    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Возвращает продолжительность книги."""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливает продолжительность книги."""
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность книги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность книги должна быть положительным числом")
        self._duration = new_duration


print(PaperBook("Букварь", "Author_paper", 300))  # PaperBook('Букварь')
print(AudioBook("Букварь", "Author_audio", 30.5))  # AudioBook('Букварь')
book_paper = PaperBook("Букварь", "Author_paper", 300)
book_audio = AudioBook("Букварь", "Author_audio", 30.5)
print(book_paper.name) # вызываем как атрибут, но срабатывает метод
print(book_audio.duration)  # вызываем как атрибут, но срабатывает метод
book_audio.duration = 40.5  # присваиваем значение атрибуту, но срабатывает метод
print(book_audio.duration)
