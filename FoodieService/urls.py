from django.conf.urls import url
from django.contrib import admin
from FoodieApp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^foodprovider/sign-in/$', auth_views.login,
        {'template_name': 'foodprovider/sign_in.html'},
        name = 'foodprovider-sign-in'),
    url(r'^foodprovider/sign-out/$', auth_views.logout,
        {'next_page': '/'},
        name = 'foodprovider-sign-out'),
    url(r'^foodprovider/$', views.foodprovider_home, name = 'foodprovider-home'),
]
