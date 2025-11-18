from django.urls import include, path
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
     # ListAPIView endpoint
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view

    # ViewSet router (CRUD)
    path('', include(router.urls)),  # Includes the routes from the BookViewSet
]

