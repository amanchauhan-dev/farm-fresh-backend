from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("farmers", FarmerViewSet)
router.register("products", ProductViewSet)
router.register("subscriptions", SubscriptionBoxViewSet)
router.register("orders", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
