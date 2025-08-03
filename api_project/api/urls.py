from django.urls import path, include
from api.views import BookList, BookViewSet, UserList, UserDetails
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
  path('books/', BookList.as_view(), name='book-list'), # Maps to the BookList view
  path('', include(router.urls)),
  path('users/', UserList.as_view(), name='all_users'),
  path('users/<int:pk>/', UserDetails.as_view(), name='user_detail')
]