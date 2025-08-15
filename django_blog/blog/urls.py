from django.urls import path
from blog.views import createFeedback_view, home_view

urlpatterns = [
    path('create/', createFeedback_view, name='create-feedback'),
    path('home/', home_view, name='home')
]
