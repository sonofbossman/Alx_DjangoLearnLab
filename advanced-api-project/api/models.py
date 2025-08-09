from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError

# Create your models here.
class Author(models.Model):
  """
  Defines the object representation of an author.
  """
  
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Book(models.Model):
  """
  Defines the object representation of a book with its author.
  """

  title = models.CharField(max_length=100)
  publication_year = models.PositiveIntegerField()
  author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

  def clean(self):
    if self.publication_year > datetime.now().year:
      raise ValidationError("Publication year cannot be in the future!")

  def __str__(self):
    return self.title