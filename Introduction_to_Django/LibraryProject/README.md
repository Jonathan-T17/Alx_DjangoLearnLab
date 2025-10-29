# LibraryProject

A basic Django project setup for learning purposes.

## How to Run

1. Install Django with `pip install django`
2. Start the project using `django-admin startproject LibraryProject`
3. Run the server: `python manage.py runserver`
4. Visit http://127.0.0.1:8000/ to view the Django welcome page.

 Utilizing the Django Admin Interface**

### **Objective**

Configure the Django Admin to manage the `Book` model from the `bookshelf` app.

---

### **Steps**

#### **Register the Book Model**

Edit **`bookshelf/admin.py`**:

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
