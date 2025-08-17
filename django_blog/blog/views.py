from django.shortcuts import render, redirect
from blog.forms import RegisterForm, ProfileForm, PostForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .models import Post

# Create your views here.
def register_view(request):
  if request.method=='POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = RegisterForm()
  return render(request, "blog/register.html", {'form': form})

def home_view(request):
  if request.method=='GET':
    return render(request, "blog/base.html")

@login_required  
def profile_view(request):
  profile = request.user.profile
  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
            form.save()
            return redirect('profile')
  else:
        form = ProfileForm(instance=profile)
    
  return render(request, 'blog/profile.html', {'form': form})

class PostListView(ListView):
   model = Post
   template_name = "blog/post_list.html"
   context_object_name = "posts"
   paginate_by = 10

class PostDetailView(DetailView):
   model = Post
   template_name = "blog/post_detail.html"
   context_object_name = "post"

class PostCreateView(LoginRequiredMixin, CreateView):
   model = Post
   form_class = PostForm
   template_name = "blog/post_form.html"
   success_url = reverse_lazy("posts")
   
   def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)

class AuthorRequiredMixin(UserPassesTestMixin):
   def test_func(self):
      obj = self.get_object()
      return obj.author == self.request.user

class PostUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
   model = Post
   form_class = PostForm
   template_name = "blog/post_form.html"

class PostDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
   model = Post
   template_name = "blog/post_confirm_delete.html"
   success_url = reverse_lazy("post-list")