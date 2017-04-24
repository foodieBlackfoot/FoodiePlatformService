from django.contrib import admin

# Register your models here.
from FoodieApp.models import Cook, Customer

admin.site.register(Cook)
admin.site.register(Customer)
