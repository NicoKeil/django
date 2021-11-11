from django.urls import path
from . import views

urlpatterns = [
	path('', views.cart, name="cart"),
	path('cart/<int:product_id>', views.addCart, name="addCart"),
]