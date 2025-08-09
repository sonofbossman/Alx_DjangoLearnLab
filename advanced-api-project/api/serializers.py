from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
  """
  Serializes all fields of the Book model.
  Includes a custom validation to the BookSerializer to 
  ensure the publication_year is not in the future.
  """

  class Meta:
    model = Book
    fields = "__all__"
  
  def validate_publication_year(self, value):
    if value > datetime.now().year:
      raise serializers.ValidationError("Publication year cannot be in the future!")
    return value

class AuthorSerializer(serializers.ModelSerializer):
  """
  Serializes all fields of the Author model, 
  and nested BookSerializer to serialize the related books dynamically.
  """
  
  books = BookSerializer(many=True, read_only=True)

  class Meta:
    model = Author
    fields = "__all__"