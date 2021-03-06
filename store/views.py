from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
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
		in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
	except Exception as e:
		raise e

	context = {
		'product': single_product,
		'in_cart': in_cart,
	}

	return render(request, 'store/product_detail.html', context)