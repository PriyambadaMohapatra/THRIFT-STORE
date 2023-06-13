from django.shortcuts import render

# Create your views here.

def sellwithus(request):
    return render(request, "sellwithus.html")

def home(request):
    return render(request, "index.html")

