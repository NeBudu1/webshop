from django.shortcuts import render
from shop.models import Products, Categories

a = "hello"
# Create your views here.
def shopview(request):
    return render(request, "index.html")
def infoview(request):
    return render(request, "info.html")
def mainview(request):
    products = Products.objects.all()
    categories = Categories.objects.all()
    return render(request, "main.html", context = {"key1":a, "products": products, "categories": categories})
