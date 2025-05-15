from django.contrib import admin
from .models import Product, Variations

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price', 'stock', 'is_available', 'modified_date')
    prepopulated_fields = {'slug': ('product_name',)}
    
    list_editable = ('price', 'stock', 'is_available')
    list_filter = ('category',)
    search_fields = ('product_name',)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')
    search_fields = ('product__product_name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Variations, VariationAdmin)
