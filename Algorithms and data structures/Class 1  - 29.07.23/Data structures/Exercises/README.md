# Exercise 1

Write code simulating a Stack of books. The class should allow you to add and remove books from the
Stack, browse titles in Stack and show the last position on the Stack. Use magic methods to
allowfor:

- adding Stacks together
- comparing Stack sizes
- Stack string representation
- stating Stack length

````python
from typing import List


class BooksStack:
    def add_new_book(self, title: str):
        pass

    def get_book(self):
        pass

    def all_books(self) -> List[str]:
        pass

````

Samples for tesing:

````
my_books = BooksStack("My Stack of Books", "Natural")
my_books.add_new_book("Cheetahs")
my_books.add_new_book("Elephants")
my_books.add_new_book("Cats")

print(my_books.all_books())
print(my_books.get_book())
print(my_books.all_books())

her_books = BooksStack("Her Stack of Books", "Natural")
her_books.add_new_book("Horses")

my_books = my_books + her_books
print(my_books.all_books())

print(my_books > her_books)
print(my_books <= her_books)

print(my_books)
print(repr(my_books))

print(len(my_books))
````

And desired output:

````
['Cheetahs', 'Elephants', 'Cats']
Cats
['Cheetahs', 'Elephants']
['Cheetahs', 'Elephants', 'Horses']
True
False
Stack: My Stack of Books with category of books: Natural
stack_name: My Stack of Books
category: Natural
books: Cheetahs Elephants Horses
3
````

# Exercise 2

## Exercise 2.1: Clients

Imagine we have a store. Implement the store's customer abstract class and 3 classes inheriting from
it.
There are three groups of customers:

- Women
- Men
- Children

Each of these groups should be addressed in a different way: women as Madam, men as Mr,
and no prefixes for children.

Each inherited class should have its own string representation.
