from django.shortcuts import render
from .models import Author, Book, Library, Librarian

# Create your views here.
def fbv_listview(request):
  try:
    books = Book.objects.all()
    context = {'books': books}
    return render(request, "relationship_app/list_books.html", context)
  except:
    return render(request, "relationship_app/not_found.html")