from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from app_post.models import Category, Post 
from app_post.serializers import UserSerializer, CategorySerializer, PostSerializer

# Create your views here.
def index(request):
    return render(request, 'app_post/index.html')

class UserView(APIView):
    
    def get(self, request, format=None):
        return Response(UserSerializer(User.objects.all(), many=True).data)

class CategoryView(APIView):
    
    def get(self, request, format=None):
        return Response(CategorySerializer(Category.objects.all(), many=True).data)

class PostView(APIView):
    
    def get(self, request, format=None):
        return Response(PostSerializer(Post.objects.all(), many=True).data)
