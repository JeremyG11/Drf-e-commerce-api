from django.db import models
from user.models import CustomUser as User


class CategoryManager(models.Manager):
    def queryset(self, category):
        products = Product.objects.filter(category=self.category)
        return products

class ProductManager(models.Manager):
    def queryset (self):
        return super(ProductManager, self).queryset().filter(is_in_stock=True)
    
    
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) 
    item_name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE, default='Admin')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=225)
    
    image = models.ImageField(upload_to='images/', default = 'images/default.png')
    is_active = models.BooleanField(default=True)
    is_in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    objects = models.Manager()
    products = ProductManager()
    
    
    class Meta:
        verbose_name_plural = 'products'
        ordering = ('-created',)
        
        
    def __str__(self):
        return self.item_name