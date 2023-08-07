import uuid
from django.shortcuts import render
from store.models import Product
from  .models import OrderItem
from rest_framework.response import Response
from rest_framework import status 
from .serializers import OrderSerializer
from .models import Order
from django.db import transaction
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
 
 
@api_view(['GET'])
def get_orders(request):
    # orders = Order.objects.all()
    orders = Order.objects.select_related('owner').prefetch_related('order_items')
    
    if not orders.exists():
        return Response([], status=status.HTTP_200_OK)
    
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_order(request, id):
    
    order = get_object_or_404(Order, pk=id)
    serializer = OrderSerializer(order)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    
    if not order:
        return Response({"Error":"The order doesn't exist" }, status=status.HTTP_404_NOT_FOUND)

    serializer = OrderSerializer(order, data=request.data, partial=True)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR )



@api_view(['DELETE'])
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if not order.is_paid:
        # Only allow deleting unpaid orders
        order.delete()
        return Response({"message": "Order deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({"error": "Cannot delete a paid order."}, status=status.HTTP_403_FORBIDDEN)



 

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def place_order(request):
    cart_items = request.data.get('items', [])  # Get the cart items from the request data

    if not cart_items:
        return Response({"Error": "Cart items are missing. Cannot place an empty order."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Generate a unique order number using UUID
        order_number = str(uuid.uuid4().hex)[:10]  # Use first 10 characters of the UUID

        # Create a new order
        order = Order.objects.create(
            owner=request.user,
            order_number=order_number,
            total_amount=0
        )

        total_amount = 0
        for item in cart_items:
            product_id = item.get('product_id')
            quantity = item.get('quantity')

            product = get_object_or_404(Product, pk=product_id)

            # Add cart item to the order
            order_item = OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                unit_price=product.price
            )

            total_amount += order_item.subtotal()

        order.total_amount = total_amount
        order.save()

        # Return the order details in the response
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
