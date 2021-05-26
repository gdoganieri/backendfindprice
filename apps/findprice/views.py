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
        category = []
        id = []
        for i in range(len(CATEGORY_CHOICES)):
            id.append(i)
            category.append(CATEGORY_CHOICES[i][0])
        categories = [{"id": t, "category": s} for t, s in zip(id, category)]
        # return (json.dumps(categories))
        return JsonResponse(categories, safe=False)