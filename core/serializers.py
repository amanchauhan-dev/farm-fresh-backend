from rest_framework import serializers
from .models import Farmer, Product, SubscriptionBox, Order


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SubscriptionBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionBox
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
