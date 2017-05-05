from django.contrib import admin

# Register your models here.
from FoodieApp.models import Cook, User

admin.site.register(User)
admin.site.register(Cook)
