# django_blog

 User Authentication System Documentation

This document explains how the User Authentication System was implemented in the django_blog project as part of Task 1.
It includes setup, configuration, file structure, and usage instructions for registration, login, logout, and user profile management.

📌 Overview

The authentication system includes:

User Registration (custom form)

User Login (Django built-in view)

User Logout

User Profile Page

Profile Editing (username + email)

CSRF protection enabled by default

Access restrictions for authenticated pages

All features follow Django’s security best practices.

📁 Project Structure (Relevant Files Only)
django_blog/
│
├── django_blog/
│   ├── settings.py
│   └── urls.py
│
├── blog/
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── models.py
│   ├── templates/
│   │   └── blog/
│   │       ├── login.html
│   │       ├── logout.html
│   │       ├── register.html
│   │       └── profile.html
│   └── admin.py
│
└── manage.py

⚙️ 1. Authentication Forms

File: blog/forms.py

UserRegisterForm extends UserCreationForm

Adds an email field

UserUpdateForm allows profile editing

🧠 2. Authentication Views

File: blog/views.py

Includes:

UserLoginView – Login page

UserLogoutView – Logout confirmation

register() – Register new users

profile() – View and edit profile (requires login)

Django automatically handles:

password hashing

CSRF protection

session management

🌐 3. URL Configuration

File: blog/urls.py

Defines:

/login/

/logout/

/register/

/profile/

These URLs link to the views described above.

🎨 4. Authentication Templates

Located in:

blog/templates/blog/

Templates created:

login.html

User login page.

logout.html

Displays logout confirmation.

register.html

User signup page with form validation.

profile.html

Users can view and update their profile.

All templates use form.as_p for structured field rendering and include CSRF tokens.

🔐 5. Authentication Settings

In django_blog/settings.py, we added:

LOGIN_REDIRECT_URL = "blog:profile"
LOGOUT_REDIRECT_URL = "blog:login"
LOGIN_URL = "blog:login"

This ensures:

After login → redirect to profile

After logout → redirect to login

If unauthorized access → redirect to login

🧪 6. Testing Instructions
Start the development server:
python manage.py runserver

1.register
2. login
3.update the profile

✔ Update username & email
✔ CSRF-protected form

🔒 7. Security Considerations

The authentication implementation uses Django’s built-in security features:

Password hashing (PBKDF2 by default)

CSRF protection on all POST forms

Session-based authentication

Access control using @login_required

Form validation to prevent invalid data submission

📘 8. How to Extend the System (Optional Enhancements)

You may optionally extend the user profile with:

Profile picture

Bio / About section

Phone number

Social links

Custom user model

## Blog Post Management (CRUD)

Routes:

- List all posts: `/posts/`
- Create new post: `/posts/new/` (authenticated)
- Post detail: `/posts/<pk>/`
- Edit post: `/posts/<pk>/edit/` (author only)
- Delete post: `/posts/<pk>/delete/` (author only)

Permissions:

- Anyone can view list and details.
- Only logged-in users can create posts.
- Only the post author can edit or delete.

Forms:

- Post creation and editing use `blog/forms.py` => `PostForm`.
- Author is set automatically in the `PostCreateView`.

Templates:

- `post_list.html`, `post_detail.html`, `post_form.html`, `post_confirm_delete.html` located at `blog/templates/blog/`.

Testing:

- Manual tests: run server and exercise each page.
- Automated tests: `python manage.py test blog`.

Notes:

- All write actions are CSRF-protected.
- Ensure your `base.html` includes links for login/logout and creating a post when authenticated.

### Comment System

- Add comment: POST to `/post/<post_pk>/comments/new/` (form located on the post detail page).
- Edit comment: `/comment/<pk>/edit/` (only comment author).
- Delete comment: `/comment/<pk>/delete/` (only comment author).
- Only authenticated users can create comments.
- Comments are listed on the post detail page; newest comments appear last (ordered by created_at).

### Tagging Feature

- Posts now support multiple tags.
- Tags are added via the “Tags (comma separated)” field in the post form.
- Tags appear on each post detail page.
- Clicking a tag filters posts by that tag: /tags/<tag_name>/

### Search Feature

- Search bar in the navigation enables searching by:
  • title
  • content
  • tag names
- Search results at /search/?q=keyword
