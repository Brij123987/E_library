from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    quantity = models.PositiveIntegerField(default=1)
    totalprice = models.FloatField(default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(( 
            self.user,
            self.content_type
            ))


