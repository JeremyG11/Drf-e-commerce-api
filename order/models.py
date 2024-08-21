from django.db import models
from store.models import Product
from user.models import CustomUser as User

# Create your models here.

class Order(models.Model):
    order_number = models.CharField(max_length=64, unique=True)
    order_date = models.DateTimeField(auto_now=True)
    order_items = models.ManyToManyField(Product, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return f"Order {self.order_number} by {self.owner}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def subtotal(self):
        # Calculate the subtotal for the order item (unit price * quantity)
        return self.unit_price * self.quantity

    def __str__(self):
        return f"OrderItem: {self.product.name} (Quantity: {self.quantity})"