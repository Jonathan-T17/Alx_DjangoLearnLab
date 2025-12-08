# Social Media API:

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
  "profile_picture":  "https://example.com/me.jpg"
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

📁 Project Structure
social_media_api/
    accounts/
        models.py
        views.py
        serializers.py
        urls.py
    social_media_api/
        settings.py
        urls.py