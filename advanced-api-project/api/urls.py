from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    # List all books (GET)
    path('books/', BookListView.as_view(), name='book-list'),

    # Create a book (POST)
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Detail view (GET)
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update view (PUT/PATCH)
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),

    # Delete view (DELETE)
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete')
]