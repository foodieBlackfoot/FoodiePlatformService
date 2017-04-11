from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from FoodieApp import views

urlpatterns = [
    # admin
    url(r'^admin/', admin.site.urls),

    # food provider
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

    # social auth
    url(r'^api/social/', include('rest_framework_social_oauth2.urls')),
    # convert-token: sign-up/sign-in
    # revoke-token: sign-out
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
