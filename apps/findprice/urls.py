from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from apps.findprice.views import ProductViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="products")
products_urlpatterns = [url("api/v1/", include(router.urls))]