from django.urls import path
from .views import (
    BookListCreateView,
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

app_name = "api"

urlpatterns = [
    # List all books (GET)
    path('books/', BookListView.as_view(), name='book-list'),

    # Create a book (POST)
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Detail view (GET)
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update view (PUT/PATCH)
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),


    # Delete view (DELETE)
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    
    # Combined List and Create view (GET, POST)
    path('books-combined/', BookListCreateView.as_view(), name='book-list-create'),

]