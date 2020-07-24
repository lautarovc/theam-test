"""theamTest URL Configuration

The definition of all the rest/ URLs is here.
The protocols provided in the the as_view methods of the views, links a protocol with a method
"""

from django.conf.urls import url, include
from django.urls import path
from .views import *

urlpatterns = [
	path('', include('rest_framework.urls')),
	path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
	# User management URLs
    path('users/', UserViewSet.as_view({'get':'list', 'post':'create'})),
	path('users/<int:pk>/', UserViewSet.as_view({'get':'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
	# Customer management URLs
    path('customers/', CustomerViewSet.as_view({'get':'list', 'post':'create'})),
	path('customers/<str:pk>/', CustomerViewSet.as_view({'get':'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]