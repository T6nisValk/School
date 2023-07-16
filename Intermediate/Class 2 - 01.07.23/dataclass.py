# Simple class
import datetime
from dataclasses import dataclass


class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def is_new_book(self):
        current = datetime.date.today().year
        return True if current - self.year < 5 else False


@dataclass  # Import it from dataclasses
class BookDS:
    name: str
    author: str
    year: int

    def is_new_book(self):
        current_year = datetime.datetime.today().year
        diff = current_year - self.year
        if diff > 5:
            return False
        return True


book_3 = BookDS("Angels and Demons", "Brown", 2000)
print(book_3.name, book_3.author, book_3.year)
book_3.year = 2003
print(book_3.year)
print(book_3.is_new_book())

print("-" * 120)
book1 = Book("Things fall apart", "Chinwe Aechieve", 1979)
print(book1.is_new_book())
book1.set_name("All things fall apart")
print(book1.name)
