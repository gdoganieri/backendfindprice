from apps.findprice.models import Product, CATEGORY_CHOICES, Scan
from apps.findprice.serializers import ProductSerializer, ScanSerializer
from django.http import JsonResponse
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ScanViewSet(viewsets.ModelViewSet):
    serializer_class = ScanSerializer
    queryset = Scan.objects.all()


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
