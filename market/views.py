from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'market/products/detail.html', {'product': product})

def categories(request):
    return {'categories': Category.objects.all()}

def all_products(request):
    products = Product.objects.all()
    return render(request, 'market/home.html', {'products' : products})
