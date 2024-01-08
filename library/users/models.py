from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'pro.jpeg', upload_to='profile_pictures', blank=True, null=True)
    address = models.CharField(max_length=2000)
    phone_no = models.IntegerField(default=0)
    user_type = models.CharField(max_length=100, default='Cust')


    def __str__(self):
        return str(self.user.username)
