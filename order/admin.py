from django.contrib import admin
from django.contrib import admin
from order.models import Order, OrderItem, Cart

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
