class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute
    
    def check_out(self):
        """Mark the book as checked out"""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Mark the book as returned/available"""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is available"""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book"""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list to store books
    
    def add_book(self, book):
        """Add a book to the library"""
        if isinstance(book, Book):
            self._books.append(book)
            return True
        return False
    
    def check_out_book(self, title):
        """Check out a book by title"""
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                if book.check_out():
                    print(f"Successfully checked out: {book.title}")
                    return True
                else:
                    print(f"Book '{book.title}' is already checked out")
                    return False
        print(f"Book '{title}' not found or not available")
        return False
    
    def return_book(self, title):
        """Return a book by title"""
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                if book.return_book():
                    print(f"Successfully returned: {book.title}")
                    return True
                else:
                    print(f"Book '{book.title}' is already available")
                    return False
        print(f"Book '{title}' not found or already available")
        return False
    
    def list_available_books(self):
        """List all available books in the library"""
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No available books in the library")
        else:
            for book in available_books:
                print(book)
    
    def find_book(self, title):
        """Find a book by title (helper method)"""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None