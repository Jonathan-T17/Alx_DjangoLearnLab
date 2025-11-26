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
