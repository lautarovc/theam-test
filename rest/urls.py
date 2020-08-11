"""theamTest URL Configuration

The definition of all the rest/ URLs is here.
The protocols provided in the the as_view methods of the views, links a protocol with a method
"""

from django.conf.urls import url, include
from django.urls import path, re_path
from .views import *

from oauth2_provider.views import *

urlpatterns = [
	# User management URLs
    re_path(r'^users/*$', UserViewSet.as_view({'get':'list', 'post':'create'})),
	re_path(r'^users/(?P<pk>\d+)/*$', UserViewSet.as_view({'get':'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
	# Customer management URLs
    re_path(r'^customers/*$', CustomerViewSet.as_view({'get':'list', 'post':'create'})),
	re_path(r'^customers/(?P<pk>\w+)/*$', CustomerViewSet.as_view({'get':'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]


# OAuth Management Views
urlpatterns += [
	re_path(r'^oauth/authorize/*$', AuthorizationView.as_view(), name="authorize"),
    re_path(r'^oauth/token/*$', TokenView.as_view(), name="token"),
    re_path(r'^oauth/applications/*$', ApplicationList.as_view(), name="list"),
    re_path(r'^oauth/applications/register/*$', ApplicationRegistration.as_view(), name="register"),
    re_path(r'^oauth/applications/(?P<pk>\d+)/*$', ApplicationDetail.as_view(), name="detail"),
    re_path(r'^oauth/applications/(?P<pk>\d+)/delete/*$', ApplicationDelete.as_view(), name="delete"),
    re_path(r'^oauth/applications/(?P<pk>\d+)/update/*$', ApplicationUpdate.as_view(), name="update"),
]
