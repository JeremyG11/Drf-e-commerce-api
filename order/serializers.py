from rest_framework import serializers
from .models import Order, OrderItem
from user.serializers import UserSerializer
from store.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    item_name = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ('item_name', 'quantity', 'unit_price')


class OrderSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'owner', 'order_items', 'order_number', 'order_date', 'total_amount', 'is_paid', 'is_delivered')
