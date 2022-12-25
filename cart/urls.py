
from django.urls import path 

from . import views

app_name = 'Cart'

urlpatterns = [
    path('', views.get_cart_items, name='get_cart_items'),
    path('add', views.cart_add, name = 'cart_add'),
]