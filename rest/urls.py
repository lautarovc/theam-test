"""theamTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path
from .views import *

urlpatterns = [
	path('', include('rest_framework.urls')),
	path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('users/', UserViewSet.as_view({'get':'list', 'post':'create'})),
	path('users/<int:pk>/', UserViewSet.as_view({'get':'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]