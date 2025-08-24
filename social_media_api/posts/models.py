from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Post(models.Model):
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="posts")
  title = models.CharField(max_length=200)
  content = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
  content = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"Comment by {self.author} on {self.post}"