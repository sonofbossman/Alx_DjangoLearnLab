from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
  author = serializers.StringRelatedField(read_only=True)
  class Meta:
    model = Post
    fields = "__all__"
    read_only_fields = ['id', 'author', 'updated_at', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
  author = serializers.StringRelatedField(read_only=True)
  post = serializers.PrimaryKeyRelatedField(read_only=True)
  class Meta:
    model = Comment
    fields = "__all__"
    read_only_fields = ['id', 'post', 'author', 'updated_at', 'created_at']