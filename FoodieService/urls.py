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
    url(r'^cook/$', views.cook_home,
        name = 'cook-home'),
    url(r'^cook/sign-in/$', auth_views.login,
        {'template_name': 'cook/sign_in.html'},
        name = 'cook-sign-in'),
    url(r'^cook/sign-out/$', auth_views.logout,
        {'next_page': '/'},
        name = 'cook-sign-out'),
    url(r'^cook/sign-up/$', views.cook_signup,
        name = 'cook-signup'),

    # Food provider dashboard urls
    url(r'^cook/account/$', views.cook_account,
        name = 'cook-account'),
    url(r'^cook/meal/$', views.cook_meal,
        name = 'cook-meal'),
    url(r'^cook/order/$', views.cook_order,
        name = 'cook-order'),
    url(r'^cook/report/$', views.cook_report,
        name = 'cook-report'),

    # Social auth
    url(r'^api/social/', include('rest_framework_social_oauth2.urls')),
    # convert-token: sign-up/sign-in
    # revoke-token: sign-out
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
