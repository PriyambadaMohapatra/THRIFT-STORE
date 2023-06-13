from django.shortcuts import render
from math import ceil
from resale.models import Product
# Create your views here.

def home(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, "index.html", params)
def clothes(request):
    return render(request, "clothes.html")
def bags(request):
    return render(request, "bags.html")
def accessories(request):
    return render(request, "accessories.html")
def shoes(request):
    return render(request, "shoes.html")
def books(request):
    return render(request, "books.html")