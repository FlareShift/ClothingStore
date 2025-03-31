from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from order.repositories.cart_repository import CartRepository
from order.repositories.order_item_repository import OrderItemRepository
from order.repositories.order_repository import OrderRepository
from order.serializers import OrderSerializer, OrderItemSerializer, CartSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderRepository.get_all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItemRepository.get_all()
    serializer_class = OrderItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = CartRepository.get_all()
    serializer_class = CartSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderRepository.get_all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=['get'])
    def total_sales(self, request):
        total = sum(order.total_price for order in OrderRepository.get_all())
        return Response({"total_sales": total})
