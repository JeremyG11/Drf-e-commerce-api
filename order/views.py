from django.shortcuts import render
from cart.models import Cart, CartItem
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .serializers import OrderSerializer
from .models import Order

class PlaceOrderView(APIView):
    def post(self, request):
        cart = Cart.objects.get(owner=request.user)

        if not cart.items.exists():
            return Response({"Error": "Cart is empty. Cannot place an empty order."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Create a new order
            order = Order.objects.create(user=request.user, total_amount=cart.total_amount)

            # Add cart items to the order
            for cart_item in cart.items.all():
                CartItem.objects.create(
                    order=order,
                    product_id=cart_item.product_id,
                    quantity=cart_item.quantity,
                    price=cart_item.price
                )
            order.save()
            # Clear the cart after placing the order
            cart.items.all().delete()

            # Return the order details in the response
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
