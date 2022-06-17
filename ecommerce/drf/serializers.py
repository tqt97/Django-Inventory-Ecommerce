from ecommerce.inventory.models import (
    Brand,
    Category,
    Media,
    Product,
    ProductAttributeValue,
    ProductInventory,
)
from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductAttributeValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        exclude = ["id"]
        depth = 2


class MediaSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ["image", "alt_text"]
        read_only = True

    def get_image(self, obj):
        return self.context["request"].build_absolute_uri(obj.image.url)


class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        readonly = True
        editable = False


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name"]
        read_only = True
        editable = False


class ProductInventorySerializer(serializers.ModelSerializer):
    # brand = BrandSerializer(many=False, read_only=True)
    # attribute = ProductAttributeValuesSerializer(source="attribute_values", many=True, read_only=True)
    # image = MediaSerializer(source="media_product_inventory", many=True, read_only=True)
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "product",
        ]
        readonly = True
        # depth = 2
