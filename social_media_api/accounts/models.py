from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

def profile_upload_to(instance, filename):
  return f"profiles/{instance.pk}/{filename}"

class CustomUser(AbstractUser):
  email = models.EmailField(unique=True, blank=False)
  bio = models.TextField(blank=True)
  fullname = models.CharField(blank=True, max_length=200)
  profile_picture = models.ImageField(upload_to=profile_upload_to, blank=True, null=True)
  followers = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='following')
  date_updated = models.DateTimeField(auto_now=True)
  date_of_birth = models.DateField(blank=True, null=True)

  def __str__(self):
    return self.username
