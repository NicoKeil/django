from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=100, unique=True)
	slug = models.CharField(max_length=100, unique=True)
	description = models.TextField(max_length=500, blank=True)
	price = models.IntegerField()
	image = models.ImageField(upload_to = 'photos/products', blank=True)
	stock = models.IntegerField()
	is_available = models.BooleanField(default=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)


	def getUrl(self):
		return reverse('product_detail', args=[self.category.id, self.id])

	def __str__(self):
		return self.name

