from django.shortcuts import render, redirect
from blog.forms import RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required

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