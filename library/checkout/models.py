from django.db import models
from django.contrib.auth.models import User
from addcart.models import CartItem
from users.models import Profile
import random

random_number = random.randint(10000,99999)


# Create your models here.

class Checkout_Detail(models.Model):
    order_id =  models.CharField(default=random_number, unique= True, max_length=99999)
    name =  models.CharField(max_length = 100)
    contact_number = models.IntegerField()
    address = models.CharField(max_length=150)
    pin_code =  models.IntegerField()


    def __str__(self):
        return str((
            self.name,
            self.order_id
        ))




