from django.db import models
from django.contrib.auth.models import User
from addcart.models import CartItem
from users.models import Profile
import random
import datetime

random_number = random.randint(10000,9999999)


# Create your models here.

class Checkout_Detail(models.Model):
    order_id =  models.CharField(default=random_number, unique= False, max_length=99999)
    name =  models.CharField(max_length = 100)
    contact_number = models.IntegerField()
    address = models.CharField(max_length=150)
    pin_code =  models.IntegerField()


    def __str__(self):
        return str((
            self.name,
            self.order_id
        ))

class Transaction(models.Model):
    trans_id = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return str((
            self.trans_id,
        ))

class Transaction_Details(models.Model):
    trans = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    orders = models.ForeignKey(Checkout_Detail, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str((
            self.trans.trans_id,
            self.orders.order_id,
            self.created_at
        ))


