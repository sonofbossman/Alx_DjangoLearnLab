from django.shortcuts import render, redirect
from accounts.forms import RegisterForm

# Create your views here.
def register_view(request):
  if request.method=='POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = RegisterForm()
  return render(request, "registration/register.html", {'form': form})

def home_view(request):
  if request.method=='GET':
    return render(request, "blog/base.html")