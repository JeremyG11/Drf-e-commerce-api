from django.contrib import admin
from store.models import Category,Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'slug', 'price','is_in_stock', 'created', 'updated']
    list_filter = ['is_in_stock', 'is_active']
    list_editable = ['price', 'is_in_stock']
    prepopulated_fields = {'slug': ('category', 'item_name')}