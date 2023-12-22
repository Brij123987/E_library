from django.urls import path, include
from checkout import views

app_name = 'checkout'

urlpatterns = [
    path('check/', views.chk_form, name='check'),
    path('check_page/',views.payment_page, name='check_page'),
    path('on_approve/',views.OnApprove, name='on_approve'),
    path('paymentsuccess/',views.PaymentSuccess, name='paymentsuccess'),
]