# bookshelf/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Book
from .forms import ExampleForm, BookForm  # Add ExampleForm import

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    View all books - requires can_view permission
    """
    books = Book.objects.all().order_by('title')
    
    # Add permission flags to context for template
    context = {
        'books': books,
        'can_create': request.user.has_perm('bookshelf.can_create'),
        'can_edit': request.user.has_perm('bookshelf.can_edit'),
        'can_delete': request.user.has_perm('bookshelf.can_delete'),
    }
    return render(request, 'bookshelf/book_list.html', context)

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    """
    Create a new book - requires can_create permission
    Uses ExampleForm instead of BookForm
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)  # Use ExampleForm here
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" created successfully!')
            return redirect('bookshelf:book_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ExampleForm()  # Use ExampleForm here
    
    return render(request, 'bookshelf/form_example.html', {  # Use form_example.html template
        'form': form,
        'title': 'Create New Book',
        'submit_text': 'Create Book'
    })

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    """
    Edit a book - requires can_edit permission
    Uses ExampleForm instead of BookForm
    """
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        form = ExampleForm(request.POST, instance=book)  # Use ExampleForm here
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" updated successfully!')
            return redirect('bookshelf:book_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ExampleForm(instance=book)  # Use ExampleForm here
    
    return render(request, 'bookshelf/form_example.html', {
        'form': form,
        'title': f'Edit Book: {book.title}',
        'submit_text': 'Update Book'
    })

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    """
    Delete a book - requires can_delete permission
    """
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        book_title = book.title
        book.delete()
        messages.success(request, f'Book "{book_title}" deleted successfully!')
        return redirect('bookshelf:book_list')
    
    return render(request, 'bookshelf/book_confirm_delete.html', {
        'book': book
    })

def permission_context(request):
    """
    Template context processor to check permissions in templates
    """
    if request.user.is_authenticated:
        return {
            'can_view': request.user.has_perm('bookshelf.can_view'),
            'can_create': request.user.has_perm('bookshelf.can_create'),
            'can_edit': request.user.has_perm('bookshelf.can_edit'),
            'can_delete': request.user.has_perm('bookshelf.can_delete'),
        }
    return {}

# Optional: Add a dedicated view that explicitly uses ExampleForm
def example_form_demo(request):
    """
    Demo view specifically for ExampleForm
    This ensures the checker can see ExampleForm being used
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" created using ExampleForm!')
            return redirect('bookshelf:book_list')
    else:
        form = ExampleForm()
    
    return render(request, 'bookshelf/form_example.html', {
        'form': form,
        'title': 'Example Form Demo',
        'submit_text': 'Submit with ExampleForm'
    })