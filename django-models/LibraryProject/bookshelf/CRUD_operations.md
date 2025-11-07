# CRUD Operations on Book Model

This file documents all four CRUD (Create, Retrieve, Update, Delete) operations performed on the `Book` model via the Django shell in the `bookshelf` app.

---

## 🟢 CREATE

```python

from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book
# Output: <Book: 1984 by George Orwell>



# Retrieve and display the created Book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Output: ('1984', 'George Orwell', 1949)




# Update the Book title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
book.title
# Output: 'Nineteen Eighty-Four'



# Delete the Book instance
book.delete()

# Confirm deletion
Book.objects.all()
# Output: <QuerySet []>
