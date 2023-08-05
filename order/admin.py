from django.contrib import admin
from .models import Order

@admin.register(Order)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['orderIdReference', 'isPaid']
 