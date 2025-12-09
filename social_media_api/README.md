# Social Media API

 Task 0: Project Setup & User Authentication

This project is part of the ALX Django LearnLab program.
In Task 0, you will build the foundation of a Social Media API using Django and Django REST Framework.

🚀 Features Implemented in This Task

Django project setup

Django REST Framework configuration

Custom user model (with bio, profile picture, followers)

Token-based authentication

User registration

User login (returns token)

Authenticated user profile endpoint

Clean and modular project structure

📦 Installation & Setup

1. Install dependencies
pip install django djangorestframework djangorestframework-simplejwt pillow
pip install djangorestframework-authtoken

2. Apply migrations
python manage.py makemigrations
python manage.py migrate

3. Run the development server
python manage.py runserver

👤 Custom User Model

The project uses a custom user model extending AbstractUser with fields:

bio

profile_picture

followers (ManyToMany to self)

🔐 Authentication Endpoints
Endpoint Method Description
/accounts/register/  POST  Create a new user
/accounts/login/  POST  Login and return token
/accounts/profile/  GET  View logged-in user profile
🧪 Example Requests
Register
POST /accounts/register/

{
  "username": "jon",
  "password": "mypassword123",
  "bio": "Hello world!",
  "profile_picture":  "<https://example.com/me.jpg>"
}

Login
POST /accounts/login/

{
  "username": "jon",
  "password": "mypassword123"
}

Returns a token.

Profile

Header:
Authorization: Token <your_token>

GET /accounts/profile/

## Posts & Comments API

Base: /api/

### Posts

- GET /api/posts/ — list posts (supports search/filter/order/pagination)
- POST /api/posts/ — create post (auth required)
- GET /api/posts/{id}/ — retrieve
- PUT/PATCH /api/posts/{id}/ — update (owner only)
- DELETE /api/posts/{id}/ — delete (owner only)
- GET /api/posts/{id}/comments/ — list post comments

### Comments

- GET /api/comments/ — list comments
- POST /api/comments/ — create comment (auth required, include `"post": <id>`)
- PUT/PATCH/DELETE /api/comments/{id}/ — modify/delete (owner only)

Authentication: Token (Authorization: Token :key)or session.

## Follow & Feed endpoints

### Follow a user

POST /accounts/follow/{user_id}/
Auth required (session or token).
Response: 200 OK on success.

### Unfollow a user

POST /accounts/unfollow/{user_id}/
Auth required.

### List followers

GET /accounts/followers/{user_id}/
Auth required.

### List following

GET /accounts/following/{user_id}/
Auth required.

### User feed

GET /api/feed/
Auth required.
Returns paginated posts from users the authenticated user follows, ordered by newest first.
