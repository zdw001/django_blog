from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save

from django.utils.text import slugify

def upload_location(instance, filename):
	"""
	saves imagefield or filefield into separate folder for each post
	also doesn't change the fies name (but allows us to change the 
	files name if we want)
	"""
	return "%s/%s" %(instance.id, filename)

class Post(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to=upload_location, 
		null=True, 
		blank=True, 
		width_field="width_field", # specifically for imagefield
		height_field="height_field") # specifically for imagefield
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self): # for python 2
		return self.title

	def __str__(self): # for python 3
		return self.title

	def get_absolute_url(self):  # better practice for url routing in templates
		return reverse("posts:detail", kwargs={"slug": self.slug})

	class Meta:
		ordering = ["-timestamp", "-updated"]

def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	"""
	goes through this before a model is saved
	"""
	if not instance.slug:
		instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)