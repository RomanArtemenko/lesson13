from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from app_post.models import Category, Post 
from app_post.serializers import UserSerializer, CategorySerializer, PostSerializer
from django.http import Http404
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

# Create your views here.
def index(request):
    return render(request, 'app_post/index.html')

class UserListView(APIView):
    """
    List all users.
    """
    def get(self, request, format=None):
        return Response(UserSerializer(User.objects.all(), many=True).data)

class UserDetailView(APIView):
    """
    Retrieve a user instance.
    """    
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        return Response(UserSerializer(user).data)

class CategoryListView(APIView):
    """
    List all categories, or create a new category.
    """        
    def get(self, request, format=None):
        return Response(CategorySerializer(Category.objects.all(), many=True).data)
    
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryDetailView(APIView):
    """
    Retrieve, update a category instance.
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        return Response(CategorySerializer(self.get_object(pk)).data)

    def patch(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class CategoryDetailViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostListView(mixins.ListModelMixin,
mixins.CreateModelMixin,
generics.GenericAPIView):
    """
    List all posts, or create a new post.
    """        
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostDetailView(APIView):
    """
    Retrieve, update or delete a post instance.
    """
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        return Response(PostSerializer(self.get_object(pk)).data)

    def patch(self, request, pk, format=None):
        post = self.get_object(pk)
        post = PostSerializer(post, data=request.data, partial=True)
        if post.is_valid():
            post.save()
            return Response(post.data)
        return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostDetailViewV2(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
