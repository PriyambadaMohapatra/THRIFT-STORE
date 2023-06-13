from django.urls import path

from . import views

urlpatterns = [
    path('',views.sellwithus, name='sellwithus'),
    path('index/',views.home, name='home'),
    
]