from django.urls import path
from .views import AddToCartView, orderListView
from . import views

urlpatterns = [
    path('',  views.orderListView),
    path('add_to_cart/', AddToCartView.as_view(), name='add_to_cart'),
]
