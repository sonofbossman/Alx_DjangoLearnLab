from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
  confirm_password = serializers.CharField(write_only=True, style={'input-type': 'password'})
  class Meta:
    model = CustomUser
    fields = ['username', 'email', 'password', 'confirm_password']
    extra_kwargs = {
      'password': { 'write_only': True }, # remove password field from API response
      'email': { 'required': True, 'unique': True }, # email field should be unique and must be included
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