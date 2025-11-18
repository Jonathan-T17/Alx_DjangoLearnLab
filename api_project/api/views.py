from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

# Create your views here.

# Existing ListAPIView
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# NEW ViewSet for CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer