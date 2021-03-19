from django.contrib import admin
from django.urls import path, include

from pages.views import home_view, contact_view, about_view
from products.views import product_delete_view,  dynamic_lookup_view


app_name = "products1"

urlpatterns = [
    path('<int:my_id>/', dynamic_lookup_view, name='product-num'),
    path('<int:my_id>/delete/', product_delete_view, name='product-delete'),
]