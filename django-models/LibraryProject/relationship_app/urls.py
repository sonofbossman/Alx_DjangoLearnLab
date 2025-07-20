
from django.urls import path
from relationship_app import views
from .views import list_books


urlpatterns = [
  path('', list_books, name='list-books'),
  path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail-cbv')
]