from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Author, Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.

class BookListView(ListView):
  model = Book
  fields = "__all__"
  template_name = "book_list.html"
  # serializer_class = BookSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(DetailView):
  model = Book
  template_name = "book_detail.html"

  # serializer_class = BookSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(CreateView):
  model = Book
  fields = "__all__"
  template_name = "book_form.html"
  success_url = "/books/"
  # serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]

class BookUpdateView(UpdateView):
  model = Book
  fields = "__all__"
  template_name = "book_form.html"
  # serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]

class BookDeleteView(DeleteView):
  model = Book
  success_url = "/books/"
  template_name = "book_confirm_delete.html"
  # serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]