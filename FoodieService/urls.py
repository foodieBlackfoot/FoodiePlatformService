from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from FoodieApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^foodprovider/$', views.foodprovider_home,
        name = 'foodprovider-home'),
    url(r'^foodprovider/sign-in/$', auth_views.login,
        {'template_name': 'foodprovider/sign_in.html'},
        name = 'foodprovider-sign-in'),
    url(r'^foodprovider/sign-out/$', auth_views.logout,
        {'next_page': '/'},
        name = 'foodprovider-sign-out'),
    url(r'^foodprovider/sign-up/$', views.foodprovider_signup,
        name = 'foodprovider-signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
