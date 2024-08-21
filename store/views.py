from rest_framework import generics
from store.models import Category, Product
from store.serializers import CategorySerializer, ProductSerializer
 
 
class CategoryListView(generics.ListCreateAPIView):
    """
    List all categories, or create a new category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer