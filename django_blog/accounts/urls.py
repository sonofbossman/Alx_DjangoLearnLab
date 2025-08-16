from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import register_view, home_view, profile_view

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('', home_view, name='home'),
    path('profile/', profile_view, name='profile'),
]
