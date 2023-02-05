class Painting:
    """Базовый класс Painting"""
    def __init__(self, author: str, name: str, price: int) -> None:
        """Инициализируем экземпляр класса Painting со следующими атрибутами"""
        self.author = author
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """Возвращает информационную строку, что картина (экземпляр класса) была создана"""
        return f'Картина "{self.name}" была создана'

    def __repr__(self) -> str:
        """Возвращает валидную строку"""
        return f'{self.__class__.__name__}({self.author!r}, {self.name!r}, {self.price!r})'

    def get_price(self) -> int:
        """Возвращает стоимость картины"""
        return self.price


class ClassicalPainting(Painting): # наследуется от базового класса Painting
    """Дочерний класс ClassicalPainting"""
    def __init__(self, author: str, name: str, price: int, technic: str, price_oil: int) -> None:
        """Инициализируем экземпляр класса ClassicalPainting со следующими атрибутами"""
        super().__init__(author, name, price)
        self.technic = technic
        self.price_oil = price_oil

    def __repr__(self) -> str:
        """Возвращает валидную питоновскую строку класса, вставив которую обратно в код, позволяет создать
        экземпляр класса ClassicalPainting"""
        return f'{self.__class__.__name__}({self.author!r},{self.name!r}, {self.price!r}, {self.technic!r}, ' \
               f'{self.price_oil!r})'

    def get_price(self) -> str:
        """Возвращает общую стоимость картины с учетом цены материала - масла"""
        total = super().get_price() + self.price_oil
        return f'Итоговая цена картины: {total}'


class DigitalPainting(Painting): # наследуется от базового класса Painting
    """Дочерний класс DigitalPainting"""
    def __init__(self, author: str, name: str, price: int, technical_recources: str) -> None:
        """Инициализируем экземпляр класса DigitalPainting со следующими атрибутами"""
        super().__init__(author, name, price)
        self.techrecources = technical_recources

    def __repr__(self) -> str:
        """Возвращает валидную питоновскую строку класса, вставив которую обратно в код, позволяет создать
                экземпляр класса DigitalPainting"""
        return f'{self.__class__.__name__}({self.author!r},{self.name!r}, {self.price!r}, {self.techrecources!r})'

    def painting_recources(self) -> str:
        """Возвращает строку с техническими ресурсами, которые были использованы при написании картины"""
        return f'Были использованы следующие ресурсы: {self.techrecources}'


if __name__ == "__main__":
    painting_1 = ClassicalPainting("Leonardo da Vinci", "Lady with ermine", 2000000, "oil", 8000)
    print(painting_1)
    print(painting_1.get_price())
    print(painting_1.__repr__())

    painting_2 = DigitalPainting("Kirill Barkov", "The ninth shaft", 200000, "computer, graphic tablet, pen")
    print(painting_2)
    print(painting_2.get_price(), painting_2.painting_recources())
    print(painting_2.__repr__())
    pass