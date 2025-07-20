from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Library, Author, Book, Librarian
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test

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

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('list-books')
  else:
    form = UserCreationForm()
  return render(request, 'relationship_app/register.html', {'form':form})  

def check_role(role):
    return lambda user: user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role

@user_passes_test(check_role('Admin'), login_url='/access-denied/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(check_role('Librarian'), login_url='/access-denied/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(check_role('Member'), login_url='/access-denied/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

def access_denied_view(request):
    return render(request, 'relationship_app/access_denied.html')