from django.conf.urls import url
from django.contrib import admin
from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete
)

urlpatterns = [
	# two ways to map URLs when using function based views
	#    url(r'^posts/$', views.post_home), # this is less preferred
	#    """
	#    when you have multiple apps being imported, this will cause problems. i.e.

	#    from users import views
	#    from posts import views

	# django won't know which view we are referring to in our URL
	#    """
	url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create), # this is better because it's more specific
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
]
