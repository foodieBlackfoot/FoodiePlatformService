from django.db import models
from django.conf import settings
from Identity.models import Cook


# Create your models here.
class Meal(models.Model):
    Cook = models.ForeignKey(Cook)
    Name = models.CharField(max_length=500)
    Description = models.CharField(max_length=500)
    Image = models.ImageField(upload_to=settings.MEAL_IMAGE_ROOT, blank=False)
    Price = models.IntegerField(default=0)

    def __str__(self):
        return self.Name
