from django.contrib.auth.models import User
from rest_framework import serializers
from app_post.models import Post, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_repr = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'is_active', 'user', 'user_repr')

class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_repr = UserSerializer(source='user', read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_repr = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'status', 'category', 'user', 'title', 'text', 'create', 'update', 'user_repr', 'category_repr')
        read_only_fields = ('create', 'update',)