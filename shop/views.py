from asyncore import readwrite

from django.shortcuts import render, redirect
from django.template.defaultfilters import length

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
    bd = request.GET.get("search")
    catnumber = request.GET.get("category")
    if catnumber:
        cat = Categories.objects.get(id = catnumber)
        catproducts = Products.objects.filter(categories = catnumber)
        return render(request, "SearchCategory.html", context = {"category": cat, "catproducts": catproducts})
    return render(request, "main.html", context = {"key1":a, "products": products, "categories": categories, "catnumber": catnumber})
def pagedetail(request, number):

    product1 = Products.objects.all()
    if number > len(product1):
        return render(request, "detailPageFail.html")
    else:
        product = Products.objects.get(id=number)
        return render(request, "detailPage.html", context = {"number": number, "product": product})

def addtocart(request, id):

    products = Products.objects.get(id=id)
    cart = request.session.get("cart", {})
    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1

    request.session["cart"] = cart
    return redirect("cart")

def cart(request):
    cart = request.session.get("cart", {})
    products = []
    total = 0

    for id, qty in cart.items():
        product = Products.objects.get(id = id)
        product.total_price = product.price*qty
        product.qty = qty
        total += product.total_price
        products.append(product)
    return render(request, "basketapp.html", {"products": products, "total": total, "key1": a})




# def categoriesSearch(request, categor):
#     categories1 = Categories.objects.all()
#     category = Categories.objects.get(id=categor)
#     return render(request, "SearchCategory.html", context = {"categor": categor, "categories": categories1})





