from django.contrib import admin

from ecommerce.inventory.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    list_filter = [
        "name",
        # "created_at",
    ]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    list_filter = [
        "category",
        # "created_at",
    ]
    prepopulated_fields = {"slug": ("name",)}
