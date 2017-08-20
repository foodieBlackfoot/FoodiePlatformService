from django.contrib import admin
from CookManagement.models import Meal, Order, OrderDetail

# Register your models here.
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(OrderDetail)
