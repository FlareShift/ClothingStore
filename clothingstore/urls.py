from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from order.views import OrderViewSet, CartViewSet, OrderItemViewSet
from product.views import ProductViewSet, CategoryViewSet, ReviewViewSet
from user.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order_items', OrderItemViewSet)
router.register(r'carts', CartViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('product.urls')),
    path('api/', include('analytics.urls')),
]
