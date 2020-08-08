from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import *

# Serializer for the User class, allows to export and import Users as JSON objects
class UserSerializer(serializers.ModelSerializer):

	# Definition of model, fields and block password from showing
	class Meta:
		model = User
		fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'password']
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

	# Reimplemented update to allow editing of id field
	def update(self, instance, validated_data):
		# Assigns current user to the lastUpdatedBy attribute
		validated_data['lastUpdatedBy'] = self.context['request'].user

		serializers.raise_errors_on_nested_writes('update', self, validated_data)
		info = serializers.model_meta.get_field_info(instance)

		old_instance = Customer.objects.get(pk=instance.id)

		# Simply set each attribute on the instance, and then save it.
		# Note that unlike `.create()` we don't need to treat many-to-many
		# relationships as being a special case. During updates we already
		# have an instance pk for the relationships to be associated with.
		m2m_fields = []
		for attr, value in validated_data.items():
			if attr in info.relations and info.relations[attr].to_many:
				m2m_fields.append((attr, value))
			else:
				setattr(instance, attr, value)
		instance.save()

		# This is done because editing the id creates another instance, NOT recommended
		# for more complex models where customer is a foreign key to another table
		if (old_instance.id != instance.id):
			old_instance.delete()

		# Note that many-to-many fields are set after updating instance.
		# Setting m2m fields triggers signals which could potentially change
		# updated instance and we do not want it to collide with .update()
		for attr, value in m2m_fields:
			field = getattr(instance, attr)
			field.set(value)

		return instance