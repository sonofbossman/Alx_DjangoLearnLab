from django.shortcuts import render, redirect

# Create your views here.
from blog.forms import FeedbackForm

def createFeedback_view(request):
  if request.method == 'POST':
    form = FeedbackForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      rating = form.cleaned_data['rating']
      comments = form.cleaned_data['comments']
      print(name, email, rating, comments)
      return redirect('home')
    else:
      return render(request, 'post_form.html', {'form': form})
  else:
    form = FeedbackForm()
    return render(request, 'post_form.html', {'form': form})

def home_view(request):
  if request.method == 'GET':
    return render(request, 'home.html')