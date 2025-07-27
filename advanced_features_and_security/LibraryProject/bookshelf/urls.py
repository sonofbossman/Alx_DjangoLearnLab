from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('books/add/', views.add_book, name='add-book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit-book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete-book'),
]