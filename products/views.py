from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

#if theres a request to products, call this request
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Products')



