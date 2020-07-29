from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, response, status, exceptions
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

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()

		# If user has been deactivated, raise 404
		if not instance.is_active:
			raise exceptions.NotFound()

		# If the user has not been deleted, deactivate (soft delete)
		instance.is_active = False
		instance.save()

		return response.Response(status=status.HTTP_204_NO_CONTENT)

#----- Model Views -----#

class CustomerViewSet(viewsets.ModelViewSet):
	"""
	Endpoint for listing and editing customers, user and staff/admin accessible.
	"""
	parser_classes = (MultiPartParser, FormParser, JSONParser,)
	permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset = Customer.objects.all().order_by('-creationDate')
	serializer_class = CustomerSerializer