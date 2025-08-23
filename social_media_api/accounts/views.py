from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .serializers import RegisterSerializer, ProfileSerializer
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RegisterView(generics.CreateAPIView):
  """
  Register a new user and create token for the user.
  """

  queryset = CustomUser.objects.all()
  serializer_class = RegisterSerializer

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    response_data = {
      'message': "Registration successful",
      'user': serializer.data
    }
    return Response(data=response_data, status=status.HTTP_201_CREATED)
  
class LogoutView(APIView):
  """
  Logout a user and destroy the user token.
  """

  permission_classes = [IsAuthenticated]

  def post(self, request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class ProfileView(generics.RetrieveUpdateAPIView):
  serializer_class = ProfileSerializer
  permission_classes = [IsAuthenticated]

  def get_object(self):
    return self.request.user