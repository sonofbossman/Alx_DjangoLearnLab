
from django.urls import path
from relationship_app import views


urlpatterns = [
  path('', views.fbv_listview, name='book-list-fbv'),
  path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail-cbv')
]