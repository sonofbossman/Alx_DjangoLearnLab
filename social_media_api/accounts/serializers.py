from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
  confirm_password = serializers.CharField(write_only=True, style={'input-type': 'password'})
  class Meta:
    model = CustomUser
    fields = ['username', 'email', 'password', 'confirm_password']
    extra_kwargs = {
      'password': { 'write_only': True }, # remove password field from API response
      'email': { 'required': True, 
                'validators': [UniqueValidator(queryset=CustomUser.objects.all())] }, # email field should be unique and must be included
    }
  
  def save(self):
    password = self.validated_data.pop('password', None) # don't save the raw password field to DB
    confirm_password = self.validated_data.pop('confirm_password', None) # don't save the confirm_password field

    if password and confirm_password:
      if password != confirm_password:
        raise serializers.ValidationError({ 'error': 'Password and confirm password did not match' })
      account = CustomUser(**self.validated_data)
      account.set_password(password)
      account.save()
      return account
    else:
      raise serializers.ValidationError({ 'error': 'Password and confirm password must be provided' })

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ['id', 'username', 'first_name', 'last_name', 'fullname', 'bio',
              'email', 'date_joined', 'date_of_birth', 'profile_picture'
              ]
    extra_kwargs = {
      'id': { 'read_only': True }, # id cannot be edited
      'date_joined': { 'read_only': True }, # date_joined cannot be edited
      'email': { 'required': True, 
                'validators': [UniqueValidator(queryset=CustomUser.objects.all())] }, # email field should be unique and must be included
    }