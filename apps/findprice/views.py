from rest_framework import viewsets
from apps.findprice.models import Product
from apps.findprice.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()



