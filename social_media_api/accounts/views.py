from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from .models import CustomUser

# Create your views here.
class RegisterView(generics.CreateAPIView):
  """
  Register a new user and create token for the user.
  """

  queryset = CustomUser.objects.all()
  serializer_class = RegisterSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
      account = serializer.save()
      serializer.data['token'] = Token.objects.get_or_create(user=account).key # get or create token for user
      serializer.data['message'] = "Registration successful" # customized response on successful creation
      return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class LogoutView(APIView):
  """
  Logout a user and destroy the user token.
  """

  def post(self, request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
