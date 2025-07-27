from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model


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

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  publication_year = models.IntegerField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    permissions = [
      ("can_view", "Can view book"),
      ("can_create", "Can create book"),
      ("can_edit", "Can edit book"),
      ("can_delete", "Can delete book"),
    ]

  def __str__(self):
    return str(self.id)