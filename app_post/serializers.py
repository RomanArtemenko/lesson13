from django.contrib.auth.models import User
from rest_framework import serializers
from app_post.models import Post, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'is_active', 'user')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'status', 'category', 'user', 'title', 'text', 'create', 'update')
        read_only_fields = ('create', 'update')