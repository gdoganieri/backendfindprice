from django.conf.urls import url, include
from django.urls import path, reverse_lazy
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from apps.findprice.views import ProductViewSet, getCategory, ScanViewSet, getProductsSet, getProductScan
router = DefaultRouter()
router.register("products", ProductViewSet, basename="products")
router.register("scans", ScanViewSet, basename="scans")
router.register("prodFilt", getProductsSet, basename="prodFilt")
router.register("prodScan", getProductScan, basename="prodScan")
products_urlpatterns = [
    url("api/v1/", include(router.urls)),
    path("categories", getCategory, name="get_category"),
    path("api/v1/users/password_reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
             template_name='backendFP/registration/password_reset_confirm.html',
            success_url = '/reset/done/',
         ),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='backendFP/registration/password_reset_complete.html'), name='password_reset_complete'),
]
