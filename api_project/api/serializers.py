from rest_framework import serializers
from api.models import Book
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
  posted_by = serializers.ReadOnlyField(source='posted_by.username')
  class Meta:
    model = Book
    fields = ('id', 'title', 'author', 'posted_by')

class UserSerializer(serializers.ModelSerializer):
  books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

  class Meta:
    model = User
    fields = ['id', 'username', 'books', 'email']