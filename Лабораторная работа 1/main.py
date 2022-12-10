import doctest


class Painting:
    """
    Документация на класс.
    Класс описывает модель картины.
    """
    def __init__(self, artist: str, name_of_painting: str) -> None:
        """
        Создание и подготовка к работе объекта "Картина"
        :param artist: Художник картины
        :param name_of_painting: Название картины
        Пример:
        >>> painting = Painting("Repin I.E.", "Duel")  # инициализация экземпляра класса
        """

        self.artist = artist
        self.name_of_painting = name_of_painting

    def get_dimension(self, length: int, width: int) -> int:
        """
        Метод, который определяет размер картины
        :param length: Длина картины (в милиметрах)
        :param width: Ширина картины (в милиметрах)
        :return: Длина и ширина картины (в милиметрах)
        :raise TypeError: Если размеры картины заданы не типом данных int
        :raise ValueError: Если размеры картины заданы отрицательными числами или равны нулю
        Пример:
        >>> painting = Painting("Repin I.E.", "Duel")
        >>> painting.get_dimension(400, 500)
        """
        if not isinstance((length and width), int):
            raise TypeError("Размер картины - длина и ширина - должен быть типа int ")
        if length and width <= 0:
            raise ValueError("Длина и ширина картины должены быть положительными и отличными от нуля числами")
        ...

    def get_technique(self, technique: str) -> None:
        """
        Метод, который определяет технику написания картины
        :param technique: Техника написания картины
        Пример:
        >>> painting = Painting("Repin I.E.", "Duel")
        >>> painting.get_technique("oil painting")
        """
        ...


class Pen:
    """
    Документация на класс.
    Класс описывает модель шариковой ручки.
    """
    def __init__(self, firm: str, ink_color: str, line_thickness: str) -> None:
        """
        Создание и подготовка к работе объекта "Шарикова ручка"
        :param firm: Фирма ручка
        :param ink_color: Цвет чернил ручки
        :param line_thickness: Толщина линии письма (в милиметрах) при использовании ручки
        Пример:
        >>> pen = Pen("Pilot", "Blue", 0.5)  # инициализация экземпляра класса
        """

        if not(0.3 <= line_thickness <= 1.5):
            raise ValueError("Введенная толщина линии письма не существует")

        self.firm = firm
        self.ink_color = ink_color
        self.line_thickness = line_thickness

    def check_work(self) -> bool:
        """
        Метод, который проверяет, работает ли ручка (пишет/ не пишет)
        :return: True (пишет) или False (не пишет)
        Пример:
        >>> pen = Pen("Pilot", "Blue", 0.5)
        >>> pen.check_work()
        """
        ...

    def get_mechanism(self, mechanism: str) -> None:
        """
        Метод, который определяет механизм ручки (автомат или не автомат)
        :param mechanism: Механизм ручки (автомат или не автомат)
        Пример:
        >>> pen = Pen("Pilot", "Blue", 0.5)
        >>> pen.get_mechanism("Automat")
        """
        ...


class Bag:
    """
    Документация на класс.
    Класс описывает модель Сумки.
    """
    def __init__(self, material: str, color: str, volume: int) -> None:
        """
        Создание и подготовка к работе объекта "Сумка"
        :param material: Материал сумки
        :param color: Цвет сумки
        :param volume: Объем сумки (в литрах)
        Пример:
        >>> bag = Bag("leather", "Black", 1.5)  # инициализация экземпляра класса
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем сумки должен быть типа int или float")

        self.material = material
        self.color = color
        self.volume = volume

    def gave_free_voluem_in_bag(self, volume, occupied_voluem) -> (int, float):
        """
        Функция которая определяет, сколько свободного места есть в сумке
        :param volume: Объем всей сумки
        :param occupied_voluem: Объем, котоый занят вещами в сумке
        :raise TypeError: Тип введенных аргументов отличен от int или float
        :raise ValueError: Аргументы должны быть строго больше нуля и volume всегда должен быть
        больше или равен occupied_voluem
        :return: Количесвто (в литрах) свободного места в сумке
        Пример:
        >>> bag = Bag("leather", "Black", 1.5)
        >>> bag.gave_free_voluem_in_bag(1.5, 0.7)
        """

        if not isinstance((volume and occupied_voluem), (int, float)):
            raise TypeError("Аргументы volume и occupied_voluem должены быть типа int или float")
        if volume and occupied_voluem <= 0:
            raise ValueError("Аргументы volume и occupied_voluem должены быть положительными и отличными от нуля числами")
        if occupied_voluem > volume:
            raise ValueError("Сумка переполнена")

        ...

    def put_someting_in_bag(self, something: str) -> None:
        """
        Положить в сумку какую-то вещь
        :param something: Какая-то вещь, которую мы хотим положить в сумку
        Пример:
        >>> bag = Bag("leather", "Black", 1.5)
        >>> bag.put_someting_in_bag("Keys")
        """

        ...

    def remove_someting_from_bag(self, something: str) -> None:
        """
        Убираем какую-то вещи из сумки.
        :param something: Какая-то вещь, которую мы хотим убрать из сумку
        Пример:
        >>> bag = Bag("leather", "Black", 1.5)
        >>> bag.remove_someting_from_bag("leaflet")
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass