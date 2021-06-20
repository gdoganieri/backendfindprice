from apps.findprice.models import Product, CATEGORY_CHOICES, Scan
from apps.findprice.serializers import ProductSerializer, ScanSerializer, ProductsCatSerializer
from django.http import JsonResponse
from rest_framework import viewsets, generics
import json
from datetime import datetime


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


class getProductsCat(viewsets.ModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = ProductsCatSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('cat')
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

class getProductScan(viewsets.ModelViewSet):
    serializer_class = ProductsCatSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        filter = self.request.query_params.get('filter')
        if filter is not None:
            filter= json.loads(filter)
            lat = filter['lat']
            long = filter['long']
            id = filter['id']
            dt = filter['dt']
            queryset = queryset.filter( scan__lat__lte=float(lat)+0.5, scan__lat__gte=float(lat)-0.5,
                                        scan__long__lte=float(long)+0.5, scan__long__gte=float(long)-0.5,
                                        id=id, scan__scan_time__lte=dt)
        return queryset