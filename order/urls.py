from django.urls import path
from . import views

urlpatterns = [
    path('',  views.get_orders, name='get_orders'),
    path('place_order/', views.place_order, name='place_order'),
    path('delete/<str>:<order_id>', views.delete_order, name='delete_order'),
]
