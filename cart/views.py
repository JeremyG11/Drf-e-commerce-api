from django.shortcuts import render
from  rest_framework.generics import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import CartItem, Cart
from store.models import Product
from .serializers import CartItemSerializer

# Create your views here.
class AddToCartView(APIView):
    def post(self, request):
        # Assuming the frontend sends product_id in the request data
        product_id = request.data.get('product_id')
        if not product_id:
            return Response({"error": "Product ID not provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cart = Cart.objects.get(owner=request.user) 
             
        except Cart.DoesNotExist:
             cart = Cart.objects.create(owner=request.user) 

        # Get the product from the database based on the product_id
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({"Error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the item already exists in the cart, if so, update the quantity
        try:
            cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
             cart_item = CartItem.objects.create(cart=cart, product_id=product_id)

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    