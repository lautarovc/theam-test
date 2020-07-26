from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from .serializers import *
from .models import *

#----- Auth Views -----#

class UserViewSet(viewsets.ModelViewSet):
    """
    Endpoint for listing and editing users, only staff/admin accessible.
    """
    parser_classes = (MultiPartParser, FormParser, JSONParser,)
    permission_classes = [permissions.IsAdminUser, TokenHasReadWriteScope]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


#----- Model Views -----#

class CustomerViewSet(viewsets.ModelViewSet):
    """
    Endpoint for listing and editing customers, user and staff/admin accessible.
    """
    parser_classes = (MultiPartParser, FormParser, JSONParser,)
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Customer.objects.all().order_by('-creationDate')
    serializer_class = CustomerSerializer