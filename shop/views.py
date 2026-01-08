from django.shortcuts import render

# Create your views here.
def shopview(request):
    return render(request, "index.html")