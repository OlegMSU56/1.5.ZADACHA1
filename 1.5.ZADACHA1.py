class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self,new_floor):
        for i in range(0, new_floor):
            if new_floor < self.number_of_floors:
                i += 1
                print(i)
        if new_floor > (self.number_of_floors):
            print("Такого этажа не существует")



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
print(h1.name, h1.number_of_floors)
h1.go_to(5)
print(h2.name, h2.number_of_floors)
h2.go_to(10)

'''
class Book:
    def __init__(self, title, author, year_of_publication):
        """
        Инициализирует объект класса Book с заданными параметрами.

        :param title: Название книги
        :param author: Автор книги
        :param year_of_publication: Год издания книги
        """
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication

    def get_info(self):
        """
        Возвращает информацию о книге в формате: 'Название, Автор (Год издания)'.
        """
        a = [1, 2, 3, 4, 5]
        return f"{self.title}, {self.author} ({self.year_of_publication})" # {a}

    def update_year(self, new_year):
        """
        Обновляет год издания книги.

        :param new_year: Новый год издания
        """
        self.year_of_publication = new_year


# Пример использования класса
book_1 = Book("Название_книги", "Автор", 2000)
print(book_1.get_info())

book_1.update_year(1870)
print(book_1.get_info())
'''