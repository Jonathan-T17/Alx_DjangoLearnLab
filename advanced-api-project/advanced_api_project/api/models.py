from django.db import models

# Create your models here.

# Author model
# Represents a writer. One author can have many books.

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


# Book model
# Each book belongs to one Author (ForeignKey relationship).

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"