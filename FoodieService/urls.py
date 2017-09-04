from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from CookManagement import views as cook_views
from Identity import views as identity_views
from api.customer import apis

urlpatterns = [
                  # Admin
                  url(r'^admin/', admin.site.urls),

                  # Cook
                  url(r'^$', identity_views.home),
                  url(r'^cook/$', identity_views.cook_home,
                      name='cook-home'),
                  url(r'^cook/sign-in/$', auth_views.login,
                      {'template_name': 'cook/sign_in.html'},
                      name='cook-sign-in'),
                  url(r'^cook/sign-out/$', auth_views.logout,
                      {'next_page': '/'},
                      name='cook-sign-out'),
                  url(r'^cook/sign-up/$', identity_views.cook_signup,
                      name='cook-signup'),
                  url(r'^cook/apply/$', identity_views.cook_apply,
                      name='apply'),

                  # Cook dashboard urls
                  url(r'^cook/account/$', cook_views.cook_account,
                      name='cook-account'),
                  url(r'^cook/menu/$', cook_views.cook_menu,
                      name='cook-menu'),
                  url(r'^cook/menu/add/$', cook_views.cook_add_meal,
                      name='cook-add-meal'),
                  url(r'^cook/menu/edit/(?P<meal_id>\d+)/$',
                      cook_views.cook_edit_meal,
                      name='cook-edit-meal'),
                  url(r'^cook/order/$', cook_views.cook_order,
                      name='cook-order'),
                  url(r'^cook/report/$', cook_views.cook_report,
                      name='cook-report'),

                  # Social auth
                  url(r'^api/social/',
                      include('rest_framework_social_oauth2.urls')),
                  # convert-token: sign-up/sign-in
                  # revoke-token: sign-out

                  # APIS for customers
                  url(r'^api/customer/cooks/$', apis.customer_get_cooks),
                  url(r'^api/customer/meals/(?P<cook_id>\d+)/$',
                      apis.customer_get_meals),
                  url(r'^api/customer/order/add/$', apis.customer_add_order),
                  url(r'^api/customer/order/latest/$',
                      apis.customer_get_latest_order)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
