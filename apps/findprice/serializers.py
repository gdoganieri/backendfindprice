
from rest_framework import serializers
from apps.findprice.models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'product_name',
            'category',
            'description'
        ]