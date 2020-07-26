from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

#----- Models -----#

class Customer(models.Model):
	"""
	Contains the customer's information and relation with users
	"""

	# Required Fields
	id = models.CharField(max_length=30, verbose_name=('Id'), primary_key=True)
	name = models.CharField(max_length=30, verbose_name=('First Name'))
	surname = models.CharField(max_length=30, verbose_name=('Last Name'))
	creationDate = models.DateField(auto_now_add=True)

	# Optional Fields

	# The photo associated with this field will be deleted on_change and on_delete by the django_cleanup module that uses those receivers
	photo = models.ImageField(storage=gd_storage, height_field=None, width_field=None, max_length=100, blank=True)

	# Relations
	createdBy = models.ForeignKey(User, related_name="created_by", on_delete=models.SET_NULL, null=True)
	lastUpdatedBy = models.ForeignKey(User, related_name="updated_by", on_delete=models.SET_NULL, null=True)