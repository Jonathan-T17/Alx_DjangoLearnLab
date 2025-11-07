from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Library, Author, UserProfile
from django.views.generic import DetailView

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.decorators import permission_required



# Create your views here.

# Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-Based View: Display details for a specific library

class LibraryDetailView(DetailView):
    model = Library
    templete_name = 'library_detail.html'
    context_object_name = 'library'




# User Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registered successful!")
            return redirect('list_books')
        else:
            form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})



# User Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                messages.success(request, f"Welcome, {username}!")
                return redirect('list_books')
            else:
                messages.error(request, "Invalid username or Password.")
        else:
            form = AuthenticationForm()
            return render(request, 'relationship_app/login.html', {'form': form})
        


# User Logout View
def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out successful!')
    return render(request, 'relationship_app/logout.html')



# Role Check Functions
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role=='Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'



# Admin View
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'user': request.user})


# Librarian View
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {'user': request.user})


# Member View
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'user': request.user})



# View to add a new book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_name = request.POST.get('author')
        author, created = Author.objects.get_or_create(name=author_name)
        Book.objects.create(title=title, author=author)
        return redirect('list_books')
    return render(request, 'relationship_app/add_book.html')


# View to edit/update a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        author_name = request.POST.get('author')
        author, created = Author.objects.get_or_create(name=author_name)
        book.author = author
        book.save()
        return redirect('list_books')
    return render(request, 'relationship_app/edit_book.html', {'book': book})


# View to delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})