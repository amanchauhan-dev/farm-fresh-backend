from django.contrib import admin
from .models import Farmer, Product, SubscriptionBox, Order


@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "farm_name", "location"]
    search_fields = ["farm_name", "location", "user__username"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category", "price", "quantity", "farmer"]
    list_filter = ["category"]
    search_fields = ["name", "farmer__farm_name"]


@admin.register(SubscriptionBox)
class SubscriptionBoxAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "frequency", "created_at"]
    list_filter = ["frequency"]
    search_fields = ["user__username"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "buyer", "product", "quantity", "scheduled_date", "delivered"]
    list_filter = ["delivered", "scheduled_date"]
    search_fields = ["buyer__username", "product__name"]
