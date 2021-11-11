from django.urls import path
from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('<int:category_id>', views.store, name="products_by_category"),
	path('<int:category_id>/<int:product_id>', views.productDetail, name="product_detail")
]