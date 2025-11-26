from django.shortcuts import render
from .models import Author, Book
from rest_framework import generics, permissions
from .serializers import AuthorSerializer, BookSerializer

# Create your views here.
"""
Generic API views for Book model.
This file defines:
- BookListView     : List all books (GET)
- BookDetailView   : Retrieve a single book by ID (GET)
- BookCreateView   : Create a book (POST)
- BookUpdateView   : Update a book (PUT/PATCH)
- BookDeleteView   : Delete a book (DELETE)

Permissions:
- List/Detail: allow any user (read-only)
- Create/Update/Delete: authenticated users only
"""


# List all books (read-only for anonymous users)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] #read-only for everyone.


# Retrieve a single book by ID (read-only for anonymous users)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] #read-only for everyone.


# Create a new book (authenticated users only)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] #only authenticated users can create.

    def perform_create(self, serializer):
        """
        Custom hook called by CreateAPIView when saving new instances.
        Use this to modify or enrich saved data. For now we just save.
        """
        serializer.save()
        


# Update an existing book (authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] #only authenticated users can update.

    def perform_update(self, serializer):
        """
        Custom hook for update behavior. We call save() to persist changes.
        You can add logging, audit-trail, etc. here.
        """
        serializer.save()



# Delete a book (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser] #only admin or staff users can delete.
