from django.db import models

# Create your models here.
from django.db import models


# Author model
# Represents a writer. One author can have many books.

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



# Book model
# Each book belongs to one Author (ForeignKey relationship).

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
