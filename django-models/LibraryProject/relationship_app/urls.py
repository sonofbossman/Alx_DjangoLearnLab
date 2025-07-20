
from django.urls import path
from relationship_app import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
  path('', list_books, name='list-books'),
  path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail-cbv'),
  path('register/', views.register, name='register'),
  path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
  path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),
  path('admin-page/', views.admin_view, name='admin-view'),
  path('librarian-page/', views.librarian_view, name='librarian-view'),
  path('member-page/', views.member_view, name='member-view'),
  path('access-denied/', views.access_denied_view, name='access-denied'),
  path('books/add/', views.add_book, name='add-book'),
  path('books/<int:pk>/edit/', views.edit_book, name='edit-book'),
  path('books/<int:pk>/delete/', views.delete_book, name='delete-book'),
]