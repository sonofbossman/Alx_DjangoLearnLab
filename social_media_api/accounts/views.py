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

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
      account = serializer.save()
      token, _ = Token.objects.get_or_create(user=account) # get or create token for user
      response_data = dict(serializer.data)
      response_data['token'] = token.key
      response_data['message'] = "Registration successful" # customized response on successful creation
      return Response(data=response_data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
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