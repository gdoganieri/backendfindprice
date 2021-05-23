
from rest_framework import serializers
from apps.findprice.models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        read_only_fields = (
            "id",
            "product_name",
            "category",
            "description",
        )
        fields = (
            "id",
            "product_name",
            "category",
            "description",
        )