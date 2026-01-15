from django.shortcuts import render

a = "hello"
# Create your views here.
def shopview(request):
    return render(request, "index.html")
def infoview(request):
    return render(request, "info.html")
def mainview(request):
    return render(request, "main.html", context = {"key1":a})