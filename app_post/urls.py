"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views
from .views import UserDetailView, UserListView, \
    CategoryDetailView, CategoryListView, CategoryDetailViewSet,\
    PostDetailView, PostListView, PostDetailViewV2

router = DefaultRouter()
router.register(r'categories', views.CategoryDetailViewSet)

urlpatterns = [
    path('', views.index , name='index'),
    url(r'api/v1.0/users/$', UserListView.as_view()),
    url(r'api/v1.0/users/(?P<pk>[0-9]+)/$', UserDetailView.as_view()),
    url(r'api/v1.0/categories/$', CategoryListView.as_view()),
    url(r'api/v1.0/categories/(?P<pk>[0-9]+)/$', CategoryDetailView.as_view()),
    url(r'api/v1.0/posts/$', PostListView.as_view()),
    url(r'api/v1.0/posts/(?P<pk>[0-9]+)/$', PostDetailView.as_view()),
    url(r'api/v2.0/', include(router.urls)),
    url(r'api/v2.0/posts/(?P<pk>[0-9]+)/$', PostDetailViewV2.as_view()),
]
