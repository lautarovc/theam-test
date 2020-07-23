from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

# Serializer for the User class, allows to export and import Users as JSON objects
class UserSerializer(serializers.HyperlinkedModelSerializer):

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
		validated_data['password'] = make_password(validated_data['password'])
		return super(UserSerializer, self).update(instance, validated_data)