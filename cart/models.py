from django.db import models
from user.models import CustomUser as User

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    @property
    def total_amount(self):
        return sum(item.price * item.quantity for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product_id = models.PositiveIntegerField() 
    quantity = models.PositiveIntegerField(default=1)
 