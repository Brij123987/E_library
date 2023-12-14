from django.urls import path, include
from registration import views
from django.contrib.auth.views import PasswordResetConfirmView

app_name = 'registration'

urlpatterns = [
# Password Reset URLs
    path('password_reset/',views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',views.CustomPasswordResetConfirmView.as_view(),name='password_confirm'),
    path('password_reset_complete/',views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

# Change Password:

    path('change_password/',views.change_password, name='change_password'),
]