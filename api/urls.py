from django.urls import include, path
from django.conf.urls import url
from . import views 
# from allauth.account.views import confirm_email
from allauth.account.views import ConfirmEmailView
from rest_auth.views import PasswordResetConfirmView

# from django.contrib.auth.views import password_reset_confirm
# urlpatterns = [
    
#     url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
#     path('rest-auth/', include('rest_auth.urls')),
#     path('rest-auth/registration/', include('rest_auth.registration.urls')),
#     path('account/', include('allauth.urls')),
# ]
# urlpatterns = [
#     # Override urls
#     url(r'^registration/account-email-verification-sent/', views.null_view, name='account_email_verification_sent'),
#     url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
#     url(r'^registration/complete/$', views.complete_view, name='account_confirm_complete'),
#     url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.null_view, name='password_reset_confirm'),
   
#     # Default urls
#     url(r'', include('rest_auth.urls')),
#     url(r'^registration/', include('rest_auth.registration.urls'))
# ]

urlpatterns = [
    # Override urls
    url(r'^registration/account-email-verification-sent/', views.null_view, name='account_email_verification_sent'),
    url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    url(r'^registration/complete/$', views.complete_view, name='account_confirm_complete'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.null_view, name='password_reset_confirm'),
    # Default urls
    url(r'', include('rest_auth.urls')),
    url(r'^', include('django.contrib.auth.urls')),

    url(r'^registration/', include('rest_auth.registration.urls'))
]