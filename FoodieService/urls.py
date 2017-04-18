from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from FoodieApp import views

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Food provider
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

    # Food provider dashboard urls
    url(r'^foodprovider/account/$', views.foodprovider_account,
        name = 'foodprovider-account'),
    url(r'^foodprovider/meal/$', views.foodprovider_meal,
        name = 'foodprovider-meal'),
    url(r'^foodprovider/order/$', views.foodprovider_order,
        name = 'foodprovider-order'),
    url(r'^foodprovider/report/$', views.foodprovider_report,
        name = 'foodprovider-report'),

    # Social auth
    url(r'^api/social/', include('rest_framework_social_oauth2.urls')),
    # convert-token: sign-up/sign-in
    # revoke-token: sign-out
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
