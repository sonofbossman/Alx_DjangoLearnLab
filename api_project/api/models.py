from django.db import models

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  posted_by = models.ForeignKey('auth.User', related_name="books", on_delete=models.CASCADE)

  def __str__(self):
    return self.title