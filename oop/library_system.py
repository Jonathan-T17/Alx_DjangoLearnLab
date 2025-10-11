class Book:
    """Base class representing a generic Book"""

    def __init__(self, title:str, author:str):
        """Initialize book with title and author"""
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title:str, author:str, file_size:int):
        super().__init__(title, author)
        self.file_size = file_size



class PrintBook(Book):
    def __init__(self, title:str, author:str, page_count:int):
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book | EBook | PrintBook):
        self.books.append(book)
    
    # def remove_book(self, book:Book):
    #     self.books.remove(book)
    
    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")

            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")

            else:
                print(f"Book: {book.title} by {book.author}")