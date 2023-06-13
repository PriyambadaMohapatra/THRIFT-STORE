from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('clothes/',views.clothes, name='clothes'),
    path('bags/',views.bags, name='bags'),
    path('accessories/',views.accessories, name='accessories'),
    path('shoes/',views.shoes, name='shoes'),
    path('books/',views.books, name='books'),
]