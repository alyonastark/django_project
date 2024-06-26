from django.contrib import admin

from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    list_filter = ('category_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('product_name', 'description')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'product', 'is_current',)
    list_filter = ('name',)
