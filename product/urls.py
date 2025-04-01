from django.urls import path
from product.views import product_list, product_detail, product_form, home, product_delete

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/add/', product_form, name='product_add'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/<int:pk>/edit/', product_form, name='product_edit'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),
]
