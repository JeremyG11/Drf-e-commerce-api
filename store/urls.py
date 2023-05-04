from django.urls import path
from store.views import CategoryListView, ProductListView

urlpatterns =[
    path('categories/',CategoryListView.as_view(), name='category' ),
    path('products/',ProductListView.as_view(), name='product')
]