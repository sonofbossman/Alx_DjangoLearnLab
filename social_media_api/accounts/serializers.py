from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class RegisterSerializer(serializers.ModelSerializer):
  # serializers.CharField()
  confirm_password = serializers.CharField(write_only=True, style={'input-type': 'password'})
  token = serializers.SerializerMethodField()
  class Meta:
    model = get_user_model()
    fields = ['username', 'email', 'password', 'confirm_password', 'token']
    extra_kwargs = {
      'password': { 'write_only': True }, # remove password field from API response
      'email': { 'required': True, 
                'validators': [UniqueValidator(queryset=CustomUser.objects.all())] }, # email field should be unique and must be included
    }
  
  def get_token(self, obj):
    token = Token.objects.create(user=obj).key
    return token
  
  def create(self, validated_data):
    password = validated_data.get('password', None)
    confirm_password = validated_data.pop('confirm_password', None) # don't save the confirm_password field
    if password and confirm_password:
      if password != confirm_password:
        raise serializers.ValidationError({ 'error': 'Password and confirm password did not match' })
      user = get_user_model().objects.create_user(**validated_data)
      return user
    else:
      raise serializers.ValidationError({ 'error': 'Password and confirm password must be provided' })


class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()
    fields = ['id', 'username', 'first_name', 'last_name', 'fullname', 'bio',
              'email', 'date_joined', 'date_of_birth', 'profile_picture', 'date_updated', 'is_active'
              ]
    extra_kwargs = {
      'email': { 'required': True, 
                'validators': [UniqueValidator(queryset=CustomUser.objects.all())] }, # email field should be unique and must be included
    }
    read_only_fields = ['id', 'date_joined', 'date_updated', 'fullname', 'is_active']