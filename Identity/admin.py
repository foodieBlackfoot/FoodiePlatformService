from django.contrib import admin

# Register your models here.
from Identity.models import Cook, User, Customer

admin.site.register(User)
admin.site.register(Cook)
admin.site.register(Customer)
