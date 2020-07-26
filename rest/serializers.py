from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import *

# Serializer for the User class, allows to export and import Users as JSON objects
class UserSerializer(serializers.ModelSerializer):

	# Definition of model, fields and block password from showing
	class Meta:
		model = User
		fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'password']
		extra_kwargs = {'password': {'write_only': True}}

	# Hashes password before calling on the create and update methods
	def create(self, validated_data):
		validated_data['password'] = make_password(validated_data['password'])
		return super(UserSerializer, self).create(validated_data)

	def update(self, instance, validated_data):
		if 'password' in validated_data:
			validated_data['password'] = make_password(validated_data['password'])
		return super(UserSerializer, self).update(instance, validated_data)


# Serializer for the Customer class, allows to export and import Customers as JSON objects
class CustomerSerializer(serializers.ModelSerializer):

	# Definition of model and fields
	class Meta:
		model = Customer
		fields = ['id', 'name', 'surname', 'photo', 'createdBy', 'lastUpdatedBy']
		read_only_fields = ['createdBy', 'lastUpdatedBy']

	# Assigns current user to the createdBy and lastUpdatedBy attributes
	def create(self, validated_data):
		validated_data['createdBy'] = self.context['request'].user
		validated_data['lastUpdatedBy'] = self.context['request'].user
		return super(CustomerSerializer, self).create(validated_data)

	# Assigns current user to the lastUpdatedBy attribute
	def update(self, instance, validated_data):
		validated_data['lastUpdatedBy'] = self.context['request'].user
		return super(CustomerSerializer, self).update(instance, validated_data)