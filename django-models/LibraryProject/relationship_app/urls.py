
from django.urls import path
from relationship_app import views
from .views import list_books, RegisterView
from django.contrib.auth import views as auth_view


urlpatterns = [
  path('', list_books, name='list-books'),
  path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail-cbv'),
  path('register/', RegisterView.as_view(), name='register'),
  path('login/', auth_view.LoginView.as_view(), name='login'),
  path('logout/', auth_view.LogoutView.as_view(), name='logout')
]