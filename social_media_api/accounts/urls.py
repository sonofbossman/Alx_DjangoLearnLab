from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, LogoutView, ProfileView

urlpatterns = [
  path('login/', obtain_auth_token, name='login'),
  path('logout/', LogoutView, name='logout'),
  path('register/', RegisterView, name='register'),
  path('profile/', ProfileView, name='profile')  
]
