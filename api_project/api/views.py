from rest_framework import generics
from api.serializers import BookSerializer 
from api.models import Book

# Create your views here.
class BookList(generics.ListAPIView,
               generics.CreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer