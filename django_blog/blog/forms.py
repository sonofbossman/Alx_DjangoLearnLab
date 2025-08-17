from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import Profile, Post

class RegisterForm(UserCreationForm):
  email = forms.EmailField(required=True)

  class Meta:
    model = User
    fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['bio', 'date_of_birth', 'profile_photo']

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'content']
    widgets = {
      "title": forms.TextInput(attrs={"class": "input", "placeholder": "Post title"}),
      "content": forms.Textarea(attrs={"rows": 8, "placeholder": "Write your post..."})
    }