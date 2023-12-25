from django.contrib import admin
from checkout.models import Checkout_Detail
from checkout.models import Transaction

# Register your models here.

admin.site.register(Checkout_Detail)
admin.site.register(Transaction)