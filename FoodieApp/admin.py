from django.contrib import admin

# Register your models here.
from FoodieApp.models import FoodProvider, Customer

admin.site.register(FoodProvider)
admin.site.register(Customer)
