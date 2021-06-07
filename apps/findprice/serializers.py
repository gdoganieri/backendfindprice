
from rest_framework import serializers
from apps.findprice.models import Product, Scan

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'product_name',
            'category',
            'description'
        ]


class ScanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scan
        fields = [
            'product',
            'scan_time',
            'user',
            'lat',
            'long',
            'price'
        ]