# Simple class
from dataclasses import dataclass


class Book:
    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def is_new_book(self, current):
        return True if current - self.year < 5 else False


@dataclass  # Import it from dataclasses
class BookDS:
    name: str
    author: str
    year: int

    def is_new_book(self, current_year):
        diff = current_year - self.year
        if diff > 5:
            return False
        return True


book1 = Book("Things fall apart", "Chinwe Aechieve", 1979)
print(book1.is_new_book(2023))
book1.set_name("All things fall apart")
print(book1.name)

book2 = BookDS("Hello", "My Name", 2020)
print(book2.is_new_book(2023))
