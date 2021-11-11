from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
	"""docstring for Category"""
	name = models.CharField(max_length=20, unique=True)
	description = models.CharField(max_length=255, blank=True)
	slug = models.CharField(max_length=100, unique=True)
	image = models.ImageField(upload_to = 'photos/categories', blank=True)
	
	class Meta:
		verbose_name = 'category' 
		verbose_name_plural = 'categories'
		
	def __str__(self):
		return self.name		