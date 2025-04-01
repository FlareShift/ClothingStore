from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets

from product.forms import ProductForm
from product.models import Product
from product.repositories.category_repository import CategoryRepository
from product.repositories.product_repository import ProductRepository
from product.repositories.review_repository import ReviewRepository
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from .NetworkHelper import NetworkHelper


class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductRepository.get_all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryRepository.get_all()
    serializer_class = CategorySerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ReviewRepository.get_all()
    serializer_class = ReviewSerializer



def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def product_form(request, pk=None):
    if pk:
        product = get_object_or_404(Product, pk=pk)
    else:
        product = None

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/product_form.html', {'form': form})


def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        return redirect('product_list')

    return render(request, 'products/product_confirm_delete.html', {'product': product})