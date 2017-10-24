from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self): # for python 2
		return self.title

	def __str__(self): # for python 3
		return self.title

	def get_absolute_url(self):  # better practice for url routing in templates
		return reverse("posts:detail", kwargs={"id": self.id})