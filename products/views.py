from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})
    

def new(request):
    return HttpResponse('New products')

def shoe(request):
    return HttpResponse('Our new shoe collection')
    