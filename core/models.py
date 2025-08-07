from django.db import models
from django.contrib.auth.models import User


class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    farm_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class Product(models.Model):
    FARM_PRODUCT_CHOICES = [
        ("fruit", "Fruit"),
        ("vegetable", "Vegetable"),
        ("dairy", "Dairy"),
        ("grain", "Grain"),
    ]
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(choices=FARM_PRODUCT_CHOICES, max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    description = models.TextField(blank=True)


class SubscriptionBox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    frequency = models.CharField(
        max_length=10, choices=[("weekly", "Weekly"), ("monthly", "Monthly")]
    )
    preferences = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    scheduled_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
