# bookshelf/forms.py
from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    ExampleForm for creating and editing Book instances
    This form demonstrates Django form capabilities with custom validation
    """
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter author name'
            }),
            'publication_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter publication year',
                'min': 1000,
                'max': 2030
            })
        }
        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'publication_year': 'Publication Year'
        }
        help_texts = {
            'publication_year': 'Enter a valid year (e.g., 2023)'
        }
    
    def clean_publication_year(self):
        """Validate publication year"""
        year = self.cleaned_data.get('publication_year')
        if year and (year < 1000 or year > 2030):
            raise forms.ValidationError("Please enter a valid year between 1000 and 2030.")
        return year
    
    def clean_title(self):
        """Validate title - ensure it's not empty and has reasonable length"""
        title = self.cleaned_data.get('title')
        if title and len(title.strip()) < 2:
            raise forms.ValidationError("Title must be at least 2 characters long.")
        return title.strip()

    def clean_author(self):
        """Validate author name"""
        author = self.cleaned_data.get('author')
        if author and len(author.strip()) < 2:
            raise forms.ValidationError("Author name must be at least 2 characters long.")
        return author.strip()
