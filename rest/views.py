from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import *

#----- Auth Views -----#

class UserViewSet(viewsets.ModelViewSet):
    """
    Endpoint for listing and editing users
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer