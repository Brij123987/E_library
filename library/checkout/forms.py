from django import forms
from checkout.models import Checkout_Detail

class Checkout_Forms(forms.ModelForm):
    class Meta:
        model = Checkout_Detail
        fields = ['name','contact_number','address','pincode']