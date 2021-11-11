from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.

def store(request, category_id=None):

	products = None
	
	if category_id != None:
		categories = get_object_or_404(Category, id=category_id)
		products = Product.objects.filter(category=categories, is_available=True)
		productsCount = products.count()
	else:
		products = Product.objects.all().filter(is_available=True)
		productsCount = products.count()

	

	context = {
		'products': products,
		'products_count': productsCount
	}

	return render(request, 'store/store.html', context)

def productDetail(request, category_id, product_id):

	try:
		single_product = Product.objects.get(category__id=category_id, id=product_id)
	except Exception as e:
		raise e

	context = {
		'product': single_product
	}

	return render(request, 'store/product_detail.html', context)