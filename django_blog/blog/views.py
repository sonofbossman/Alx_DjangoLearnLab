from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import RegisterForm, ProfileForm, PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .models import Post, Comment
from django.db.models import Q

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

   def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["comment_form"] = CommentForm()
        return ctx

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

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs["post_pk"])
        form.instance.post = post
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return response  # redirects to comment.get_absolute_url() -> post detail

    def get_template_names(self):
        # If you want a separate page for comment create, return ['blog/comment_form.html']
        # But we'll submit from the post detail template, so not used directly.
        return ["blog/comment_form.html"]

# --- Only the comment author can edit/delete ---
class CommentAuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class CommentUpdateView(LoginRequiredMixin, CommentAuthorRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

class CommentDeleteView(LoginRequiredMixin, CommentAuthorRequiredMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def get_success_url(self):
        return self.object.post.get_absolute_url()
    
class PostSearchView(ListView):
    model = Post
    template_name = "blog/post_search_results.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q", "").strip()
        if not q:
            return qs.none()
        filters = Q(title__icontains=q) | Q(content__icontains=q)
        try:
            # If using taggit
            filters |= Q(tags__name__icontains=q)
        except Exception:
            pass
        return qs.filter(filters).distinct()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["q"] = self.request.GET.get("q", "")
        return ctx