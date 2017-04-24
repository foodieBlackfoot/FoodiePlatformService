from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cook(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cook')
    Name = models.CharField(max_length=500)
    Description = models.CharField(max_length=500)
    Rating = models.CharField(max_length=500)
    Tag = models.CharField(max_length=500)
    Address = models.CharField(max_length=500)
    Phone = models.CharField(max_length=500)
    Logo = models.ImageField(upload_to='cook_logo/', blank=False)

    def __str__(self):
        return self.Name

class Customer(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    Avatar = models.CharField(max_length=500)
    Phone = models.CharField(max_length=500)
    Address = models.CharField(max_length=500)

    def __str__(self):
        return self.user.get_full_name()
