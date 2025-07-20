
from django.urls import path
from relationship_app import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
  path('', list_books, name='list-books'),
  path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail-cbv'),
  path('register/', views.register, name='register'),
  path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
  path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout')
]