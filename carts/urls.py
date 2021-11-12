from django.urls import path
from . import views

urlpatterns = [
	path('', views.cart, name="cart"),
	path('cart/<int:product_id>', views.addCart, name="addCart"),
	path('remove/<int:product_id>', views.removeCart, name="removeCart"),
	path('delete/<int:product_id>', views.deleteCart, name="deleteCart"),
]