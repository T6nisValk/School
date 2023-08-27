class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}"


book_1 = Book("I don't know any books", "Important Author", 2023)
print(book_1)
