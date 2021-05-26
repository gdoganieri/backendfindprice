from rest_framework import viewsets
from apps.findprice.models import Product, CATEGORY_CHOICES
from apps.findprice.serializers import ProductSerializer
from django.http import HttpResponse, JsonResponse
import json

class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


def getCategory(request):
    if request.method == 'GET':
        categories = {}
        for i in range(len(CATEGORY_CHOICES)):
            categories[i] = CATEGORY_CHOICES[i][1]

        return JsonResponse(categories)