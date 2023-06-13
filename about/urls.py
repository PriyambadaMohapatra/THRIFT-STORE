from django.urls import path

from . import views

urlpatterns = [
    path('',views.about, name='about'),
    path('index/',views.home, name='home'),
    
]