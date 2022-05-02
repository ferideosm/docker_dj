
from django.contrib import admin

from  .models import Product, Stock, StockProduct

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')

@admin.register(Stock)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'address')

@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'stock', 'product', 'quantity', 'price')

