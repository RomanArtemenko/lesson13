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
from rest_framework.authtoken import views as view_auth
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view


from . import views

API_TITLE = 'Post API'
API_DESCRIPTION = 'A Web API for creating, editing and viewing.'

schema_view = get_swagger_view(title=API_TITLE)

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', views.index , name='index'),
    path('api/v1.0/', include(router.urls)),
    path('api/v1.0/map/', schema_view, name='map-api'),
    path('api/v1.0/docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    
]

urlpatterns += [
    url(r'^api-token-auth/', view_auth.obtain_auth_token)
]