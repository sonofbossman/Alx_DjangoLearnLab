from rest_framework import generics
from .serializers import BookSerializer, UserSerializer 
from api.models import Book
from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class BookList(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  authentication_classes = [TokenAuthentication]
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  authentication_classes = [TokenAuthentication]
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

  def perform_create(self, serializer):
    return serializer.save(posted_by=self.request.user)

class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  authentication_classes = [TokenAuthentication]
  permission_classes = [permissions.IsAdminUser]

class UserDetails(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  authentication_classes = [TokenAuthentication]
  permission_classes = [permissions.IsAdminUser]