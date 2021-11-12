from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def addCart(request, product_id):

	product = Product.objects.get(id=product_id)

	try:
		cart = Cart.objects.get(cart_id=_cart_id(request))
	except Cart.DoesNotExist:
		cart = Cart.objects.create(
			cart_id =  _cart_id(request)
		)

	cart.save()

	try:
		cart_item = CartItem.objects.get(product=product, cart=cart)
		cart_item.quantity += 1 
		cart_item.save()
	except CartItem.DoesNotExist:
		cart_item = CartItem.objects.create(
			product = product,
			quantity = 1,
			cart = cart 
		)
		cart_item.save()

	return redirect('cart')

#Creat a new Session 
def _cart_id(request):
	cart = request.session.session_key

	if not cart:
		cart = request.session.create()

	return cart

def cart(request, total=0, quantity=0, cart_items=None):

	try:
		cart = Cart.objects.get(cart_id=_cart_id(request))
		cart_items = CartItem.objects.filter(cart=cart, is_active=True)
		for cart_item in cart_items:
			total += (cart_item.product.price * cart_item.quantity)
			quantity += cart_item.quantity
	except ObjectDoesNotExist:
		pass #Solo ignora el except

	context = {
		'total': format(total, '.2f'),
		'quantity': format(quantity, '.2f'),
		'cart_items': cart_items,
		'tax': format(total * 0.21, '.2f'),
		'sub_total': format(total * 1.21, '.2f')
	}

	return render(request, "store/cart.html", context)

def removeCart(request, product_id):
	cart = Cart.objects.get(cart_id=_cart_id(request))
	product = get_object_or_404(Product, id=product_id)
	cart_item = CartItem.objects.get(product=product, cart=cart)

	if cart_item.quantity > 1:
		cart_item.quantity -= 1
		cart_item.save()
	else:
		cart_item.delete()

	return redirect("cart")

def deleteCart(request, product_id):
	cart = Cart.objects.get(cart_id=_cart_id(request))
	product = get_object_or_404(Product, id=product_id)
	cart_item = CartItem.objects.get(product=product, cart=cart)
	cart_item.delete()

	return redirect("cart")