from django.contrib import admin

from ecommerce.inventory.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    list_filter = [
        "name",
        # "created_at",
    ]
    prepopulated_fields = {"slug": ("name",)}
