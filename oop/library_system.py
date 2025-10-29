class Book:
    """Base class representing a generic Book"""

    def __init__(self, title: str, author: str):
        """Initialize book with title and author"""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of Book"""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation of EBook"""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation of PrintBook"""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    # def remove_book(self, book:Book):
    #     self.books.remove(book)
    
    def list_books(self):
        for book in self.books:
            print(book)  # This will automatically call the appropriate __str__ method