from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Author, Book, Librarian
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
def list_books(request):
  try:
    books = Book.objects.all()
    context = {'books': books}
    return render(request, "relationship_app/list_books.html", context)
  except:
    return render(request, "relationship_app/not_found.html")

class LibraryDetailView(DetailView):
  model = Library
  template_name = "relationship_app/library_detail.html"
  context_object_name = 'library'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['books'] = self.object.books.all()
    return context
  
class RegisterView(FormView):
  template_name = 'registration/register.html'
  form_class = UserCreationForm
  success_url = reverse_lazy('login')

  def form_valid(self, form):
    form.save()
    return super().form_valid(form)