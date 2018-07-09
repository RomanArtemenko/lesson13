from django.contrib.auth.models import User
from rest_framework import serializers
from app_post.models import Post, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=200)
    is_active = serializers.BooleanField()
    user = serializers.IntegerField(source='user_id')

class PostSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Post.STATUSES, default=Post.STATUS_DRAFT)
    # category = serializers.IntegerField(source='category_id')
    category = CategorySerializer(required=True)
    user = serializers.IntegerField(source='user_id', read_only=True)
    title = serializers.CharField(max_length=255, required=True)
    text = serializers.CharField(max_length=1024)
    create = serializers.DateTimeField(read_only=True)
    update = serializers.DateTimeField(read_only=True)
 
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.category = validated_data.get('category', instance.category)
        instance.user = validated_data.get('user', instance.user) 
        instance.title = validated_data.get('title', instance.title) 
        instance.text = validated_data.get('text', instance.text)
        instance.create = validated_data.get('create', instance.create)
        instance.update = validated_data.get('update', instance.update)
        instance.save()
        return instance

    def create(self, instance, validated_data):
        return Post.objects.create(**validated_data)