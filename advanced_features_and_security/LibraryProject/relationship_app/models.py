from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CustomUserManager(BaseUserManager):
  def create_user(self, username, email, password=None, **extra_fields):
    if not email:
      raise ValueError("Users must have an email address")
    email = self.normalize_email(email)
    user = self.model(username=username, email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self, username, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if not password:
      raise ValueError("Superusers must have a password")
    return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
  date_of_birth = models.DateField(null=True, blank=True)
  profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
  objects = CustomUserManager()

  def __str__(self):
    return self.username

User = get_user_model()

class Author(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
  publication_year = models.IntegerField()

  class Meta:
    permissions = [
      ("can_add_book", "Can add a book"),
      ("can_change_book", "Can change book details"),
      ("can_delete_book", "Can delete a book"),
    ]
  
  def __str__(self):
    return self.title

class Library(models.Model):
  name = models.CharField(max_length=100)
  books = models.ManyToManyField(Book, related_name='libraries')

  def __str__(self):
    return self.name

class Librarian(models.Model):
  name = models.CharField(max_length=100)
  library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

  def __str__(self):
    return self.name

class UserProfile(models.Model):
  ROLE_CHOICES = (
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
  )
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  role = models.CharField(max_length=20, choices=ROLE_CHOICES)

  def __str__(self):
    return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)