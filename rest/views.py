from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from .serializers import *

#----- Auth Views -----#

class UserViewSet(viewsets.ModelViewSet):
    """
    Endpoint for listing and editing users
    """
    permission_classes = [permissions.IsAdminUser, TokenHasReadWriteScope]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer