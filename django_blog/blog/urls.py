from django.urls import path
from django.contrib.auth import views as auth_views
from blog.views import (register_view, home_view, profile_view,
                        PostListView, PostDetailView, PostCreateView,
                        PostUpdateView, PostDeleteView
                        )

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('', home_view, name='home'),
    path('profile/', profile_view, name='profile'),
    path("posts/", PostListView.as_view(), name="posts"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete")
]
