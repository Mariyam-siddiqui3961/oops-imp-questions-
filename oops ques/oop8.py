# Composition:
# Write python code create classes for “Author” and “Book.”
# The “Book” class should have an “Author” object as an
# attribute, demonstrating composition.

class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def __str__(self):
        return f"Author: {self.name}, Nationality: {self.nationality}"

class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author  # Author object as attribute
        self.year_published = year_published

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author.name}, Year Published: {self.year_published}"

# Example usage
author1 = Author("J.K. Rowling", "British")
book1 = Book("Harry Potter and the Philosopher's Stone", author1, 1997)

print(book1)
