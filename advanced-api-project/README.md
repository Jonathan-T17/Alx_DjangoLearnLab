# advanced-api-project API - Books

Endpoints (prefix /api/):

- GET /api/books/                  -> list all books (public)
- POST /api/books/create/          -> create a book (authenticated)
- GET /api/books/<pk>/             -> retrieve book by id (public)
- PUT/PATCH /api/books/<pk>/update/-> update book (authenticated)
- DELETE /api/books/<pk>/delete/   -> delete book (authenticated)

Authentication:

- Use TokenAuthentication or SessionAuthentication as configured in settings.py.

Validation:

- BookSerializer validates publication_year (cannot be in the future).

Testing:

- Use curl or Postman. Example curl commands are in the developer docs.

## Advanced API Project (Django REST Framework)

This project demonstrates advanced Django REST Framework usage, including:

- Custom models & serializers  
- Nested serializers  
- Generic class-based views  
- Filtering, searching & ordering  
- Permissions  
- Automated tests (pytest)  
- Postman API collection  

---

## 🚀 Features Implemented

### ✔ Models

- **Author**
- **Book** (with FK to Author)

### ✔ Serializers

- `BookSerializer` with validation  
- `AuthorSerializer` with nested books  

### ✔ Filtering / Searching / Ordering

The endpoint:

```
GET /api/books/
```

supports:

| Feature | Example |
|--------|---------|
| Filter by title | `/api/books/?title=Python` |
| Filter by author | `/api/books/?author__name=John` |
| Search | `/api/books/?search=django` |
| Ordering | `/api/books/?ordering=title` |
| Reverse ordering | `/api/books/?ordering=-publication_year` |

---

## 🧪 Testing Instructions

Run all tests:

```
pytest
```

Test file is located at:

```
api/tests/test_book_api.py
```

Included test cases:

- Filtering by title  
- Searching  
- Ordering  
- Filtering by author name  

---

## 🔧 Postman Collection

A complete Postman collection is included in:

```
postman/advanced_api_collection.json
```

You can import it directly into Postman.

---

## ▶ Run Server

```
python manage.py runserver
```

---

## 📁 Project Structure

```
advanced-api-project/
│
├── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests/
│       └── test_book_api.py
│
├── advanced_api_project/
│   ├── settings.py
│   └── urls.py
│
└── README.md
```

---

## 📝 Notes

Filtering, searching, and ordering are powered by:

- `django-filter`
- DRF SearchFilter
- DRF OrderingFilter

Be sure `django_filters` is added to `INSTALLED_APPS`.

---

## ✔ Author

Created by **Jonathan Twizere** as part of the **ALX Django Learning Lab**.

## Running Tests

Run all API tests:
    python manage.py test api

Tests cover:

- CRUD operations
- Filtering
- Search
- Ordering
- Permissions
- Status codes
- Response correctness
