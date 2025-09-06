from django.db import models
from django.conf import settings

class ServiceCategory(models.Model):
    name = models.CharField(max_length = 80, unique = True)
    description = models.TextField(blank=True)
    def __str__(self): return self.name

class ServiceRequest(models.Model):
    STATUS = [
        ("new", "New"),
        ("scheduled", "Scheduled"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "requests")
    category = models.ForeignKey(ServiceCategory, on_delete = models.PROTECT)
    title = models.CharField(max_length = 120)
    description = models.TextField()
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=20, choices = STATUS, default = "new")
    quoted_price = models.DecimalField(max_digits = 9, decimal_places=2, null = True, blank = True)
    scheduled_date = models.DateField(null=True, blank=True)

