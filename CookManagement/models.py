from django.db import models
from django.conf import settings
from django.utils import timezone

from Identity.models import Cook, Customer


class Meal(models.Model):
    Cook = models.ForeignKey(Cook)
    Name = models.CharField(max_length=500)
    Description = models.CharField(max_length=500)
    Image = models.ImageField(upload_to=settings.MEAL_IMAGE_ROOT, blank=False)
    Price = models.IntegerField(default=0)

    def __str__(self):
        return self.Name


class Order(models.Model):
    CREATED = 0
    COOKING = 1
    READY = 2
    ONTHEWAY = 3
    DELIVERED = 4
    COMPLETED = 5
    CANCELED = 6

    STATUS_CHOICES = (
        (CREATED, "Created"),
        (COOKING, "Cooking"),
        (READY, "Ready"),
        (ONTHEWAY, "On the way"),
        (DELIVERED, "Delivered"),
        (COMPLETED, "Completed"),
        (CANCELED, "Canceled"),
    )

    Customer = models.ForeignKey(Customer)
    Cook = models.ForeignKey(Cook)
    Address = models.CharField(max_length=500)
    TotalPrice = models.IntegerField()
    Status = models.IntegerField(choices=STATUS_CHOICES)
    CreatedTime = models.DateTimeField(default=timezone.now)
    PickedTime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class OrderDetail(models.Model):
    Order = models.ForeignKey(Order, related_name="order_detail")
    Meal = models.ForeignKey(Meal)
    Quantity = models.IntegerField()
    SubTotalPrice = models.IntegerField()

    def __str__(self):
        return str(self.id)