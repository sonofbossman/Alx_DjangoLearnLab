from rest_framework import generics
from .serializers import BookSerializer 
from api.models import Book
from rest_framework import viewsets, generics

# Create your views here.
class BookList(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer