from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Author, Book
from .serializers import BookSerializer
from django.db.models import Q
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class BookListView(ListView):
  model = Book
  template_name = 'book_list.html'
  context_object_name = 'books'

  def get_queryset(self):
    queryset = super().get_queryset()

    # Filtering
    author = self.request.GET.get('author')
    publication_year = self.request.GET.get('publication_year')
    if author:
        queryset = queryset.filter(author__iexact=author)
    if publication_year:
        queryset = queryset.filter(publication_year=publication_year)

    # Searching
    search_term = self.request.GET.get('search')
    if search_term:
        queryset = queryset.filter(
            Q(title__icontains=search_term) |
            Q(author__icontains=search_term)
        )

    # Ordering
    ordering = self.request.GET.get('ordering')
    if ordering:
        queryset = queryset.order_by(ordering)

    return queryset

class BookDetailView(DetailView):
  model = Book
  template_name = "book_detail.html"
  context_object_name = 'book'

  # serializer_class = BookSerializer

class BookCreateView(LoginRequiredMixin, CreateView):
  model = Book
  fields = "__all__"
  template_name = "book_form.html"
  success_url = "/books/"
  # serializer_class = BookSerializer

class BookUpdateView(LoginRequiredMixin, UpdateView):
  model = Book
  fields = "__all__"
  template_name = "book_form.html"
  # serializer_class = BookSerializer
  success_url = "/books/"

class BookDeleteView(LoginRequiredMixin, DeleteView):
  model = Book
  success_url = "/books/"
  template_name = "book_confirm_delete.html"
  # serializer_class = BookSerializer