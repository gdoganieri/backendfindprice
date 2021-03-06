import datetime
import json

import requests
from apps.findprice.models import Product, CATEGORY_CHOICES, Scan, User
from apps.findprice.serializers import ProductSerializer, ScanSerializer, ProductsCatSerializer, \
    ScansForProductSerializer
from django.contrib.auth.forms import SetPasswordForm
from django.http import JsonResponse
from django.shortcuts import render
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

class getProductsSet(viewsets.ModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = ProductsCatSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('cat')
        id = self.request.query_params.get('id')
        if category is not None:
            queryset = queryset.filter(category=category)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset


class getProductScan(viewsets.ModelViewSet):
    serializer_class = ScansForProductSerializer

    def get_queryset(self):
        queryset = Scan.objects.all()
        filter = self.request.query_params.get('filter')
        if filter is not None:
            filter = json.loads(filter)
            lat = filter['lat']
            long = filter['long']
            id = filter['id']
            dt = filter['dt']
            if(id== '*'):
                print(id)
                pdt = datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S.%fZ") - datetime.timedelta(days=7)
                queryset = queryset.filter(lat__lte=float(lat) + 0.5, lat__gte=float(lat) - 0.5,
                    long__lte=float(long) + 0.5, long__gte=float(long) - 0.5,
                    scan_time__lt=dt, scan_time__gt=pdt).order_by('-scan_time')
            else:
                queryset = queryset.filter(lat__lte=float(lat) + 0.5, lat__gte=float(lat) - 0.5,
                                           long__lte=float(long) + 0.5, long__gte=float(long) - 0.5,
                                           product=id, scan_time__lt=dt).order_by('-scan_time')[:10]


        return queryset
