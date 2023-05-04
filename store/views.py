from rest_framework import generics
from store.models import Category, Product
from store.serializer import CategorySerializer, ProductSerializer
 
 
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer