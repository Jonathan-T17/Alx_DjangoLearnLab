from django.contrib import admin

# Register your models here.
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display title, author, and publication_year in the list view
    list_display = ('title', 'author', 'publication_year')

     # Filters for better admin interface
    list_filter = ('publication_year', 'author')

    # Enable search capabilities
    search_fields = ('title', 'author')
