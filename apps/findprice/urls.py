from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.findprice.views import ProductViewSet, getCategory, ScanViewSet, getProductsSet, getProductScan

router = DefaultRouter()
router.register("products", ProductViewSet, basename="products")
router.register("scans", ScanViewSet, basename="scans")
router.register("prodFilt", getProductsSet, basename="prodFilt")
router.register("prodScan", getProductScan, basename="prodScan")

products_urlpatterns = [
    url("api/v1/", include(router.urls)),
    path("categories", getCategory, name="get_category")
]
