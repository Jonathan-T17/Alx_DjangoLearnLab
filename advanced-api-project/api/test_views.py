from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User


class BookAPITest(APITestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        logged_in = self.client.login(username="testuser", password="testpass")
        print("LOGIN STATUS:", logged_in)


        # Create test authors
        self.author1 = Author.objects.create(name="John Doe")
        self.author2 = Author.objects.create(name="Alice Writer")

        # Create test books
        self.book1 = Book.objects.create(
            title="Python Basics",
            author=self.author1,
            publication_year=2020
        )
        self.book2 = Book.objects.create(
            title="Advanced Django",
            author=self.author2,
            publication_year=2022
        )

        self.client = APIClient()

    # ----------------------
    # GET LIST
    # ----------------------
    def test_book_list(self):
        url = reverse("api:book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # ----------------------
    # GET DETAIL
    # ----------------------
    def test_book_detail(self):
        url = reverse("api:book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Python Basics")

    # ----------------------
    # CREATE BOOK (AUTH REQUIRED)
    # ----------------------
    def test_create_book(self):
        self.client.login(username="tester", password="password123")

        url = reverse("api:book-create")
        data = {
            "title": "New Book",
            "author": self.author1.id,
            "publication_year": 2021
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_requires_auth(self):
        url = reverse("api:book-create")
        data = {
            "title": "Unauthorized Book",
            "author": self.author1.id,
            "publication_year": 2021
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ----------------------
    # UPDATE BOOK
    # ----------------------
    def test_update_book(self):
        self.client.login(username="tester", password="password123")

        url = reverse("api:book-update", args=[self.book1.id])
        data = {
            "title": "Updated Title",
            "author": self.author1.id,
            "publication_year": 2023
        }

        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    # ----------------------
    # DELETE BOOK
    # ----------------------
    def test_delete_book(self):
        url = reverse("api:book-delete", args=[self.book2.id])

        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(url)
    
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())


    # ----------------------
    # FILTER TEST
    # ----------------------
    def test_filter_books_by_year(self):
        url = reverse("api:book-list")
        response = self.client.get(url, {"publication_year": 2020})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # ----------------------
    # SEARCH TEST
    # ----------------------
    def test_search_books(self):
        url = reverse("api:book-list")
        response = self.client.get(url, {"search": "Python"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Python Basics")

    # ----------------------
    # ORDERING TEST
    # ----------------------
    def test_order_books(self):
        url = reverse("api:book-list")
        response = self.client.get(url, {"ordering": "title"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, sorted(titles))
