from django.db import models
from store.models import Product
from user.models import CustomUser as User

# Create your models here.

class Order(models.Model):
    order_number = models.CharField(max_length=64, unique=True)
    oder_date = models.DateTimeField(auto_now=True)
    order_items = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
        
  
        
    