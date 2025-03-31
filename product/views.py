from django.shortcuts import render
from rest_framework import viewsets
from product.repositories.category_repository import CategoryRepository
from product.repositories.product_repository import ProductRepository
from product.repositories.review_repository import ReviewRepository
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductRepository.get_all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryRepository.get_all()
    serializer_class = CategorySerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ReviewRepository.get_all()
    serializer_class = ReviewSerializer
