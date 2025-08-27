from django.db import models
from django.conf import settings
import uuid

class Listing(models.Model):
    APARTMENT_TYPE_CHOICES = [
        ("studio", "Studio"),
        ("1_bed", "1 Bedroom"),
        ("2_bed", "2 Bedroom"),
    ]

    VACANT_TYPE_CHOICES = [
        ("single", "Single"),
        ("shared", "Shared"),
    ]

    listing_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    apartment_type = models.CharField(max_length=20, choices=APARTMENT_TYPE_CHOICES)
    duration = models.CharField(max_length=50)
    vacant_type = models.CharField(max_length=10, choices=VACANT_TYPE_CHOICES)

    def __str__(self):
        return self.title

class Request(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    request_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="requests")
    seeker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="requests")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    request_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request {self.pk} for {self.listing}"
