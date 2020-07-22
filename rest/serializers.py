from django.contrib.auth.models import User
from rest_framework import serializers

# Serializer for the User class, allows to export Users as JSON objects
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
