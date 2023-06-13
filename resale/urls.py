from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ResaleHome"),
    path("search/", views.search, name="RSearch"),
    path("products/<int:myid>", views.productView, name="RProductView"),
    path("checkout/", views.checkout, name="RCheckout"),
    path("form/", views.form, name="RForm"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("succes/", views.succes, name="succes"),
    path("payment/", views.payment, name="payment"),

]
