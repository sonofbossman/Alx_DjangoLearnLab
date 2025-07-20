
from django.urls import path
from relationship_app import views


urlpatterns = [
  path('', views.fbv_listview, name='all_books')
]