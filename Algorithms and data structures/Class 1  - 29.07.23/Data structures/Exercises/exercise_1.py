class BookStack:
    def __init__(self, stack_name, category=None):
        self.stack_name = stack_name
        self.category = category
        self.stack = []

    def add_new_book(self, title):
        self.stack.append(title)

    def get_book(self):
        return self.stack.pop()

    def all_books(self):
        return self.stack

    def __add__(self, other_stack):
        new = BookStack(self.stack_name, self.category)
        new.stack = self.stack + other_stack.stack
        return new

    # def __add__(self, other_stack):
    #     new_stack = BookStack(self.stack_name, self.category)
    #     books_to_add = self.stack + other_stack.stack
    #     for book in books_to_add:
    #         new_stack.add_new_book(book)
    #     return new_stack

    def __gt__(self, other_stack):
        return len(self.stack) > len(other_stack.stack)

    def __le__(self, other_stack):
        return len(self.stack) <= len(other_stack.stack)

    def __str__(self):
        return f"Stack: {self.stack_name} with category of books: {self.category}"

    def __repr__(self):
        return f"stack_name: {self.stack_name}\n" \
               f"category: {self.category}\n" \
               f"books: {' '.join(self.stack)}"

    def __len__(self):
        return len(self.stack)


my_books = BookStack("My stack of books", "Natural")

my_books.add_new_book("Cheetahs")
my_books.add_new_book("Elephants")
my_books.add_new_book("Cats")

print(my_books.all_books())
print(my_books.get_book())
print(my_books.all_books())

her_books = BookStack("Her stack of books", "Natural")
her_books.add_new_book("Horses")

my_books = my_books + her_books
print(my_books.all_books())

print(my_books > her_books)
print(my_books <= her_books)

print(my_books)
print(repr(my_books))

print(len(my_books))
