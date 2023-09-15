from django.db import models

# Create your models here.

class Newspaper(models.Model):
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=500)
    item_price = models.IntegerField()

    def __str__(self):
        return self.item_name

class Comic(models.Model):
    comic_name = models.CharField(max_length=50)
    comic_desc = models.CharField(max_length=500)
    comic_price = models.IntegerField()

    def __str__(self):
        return self.comic_name

class Magazine(models.Model):
    magazine_name = models.CharField(max_length=50)
    magazine_desc = models.CharField(max_length=500)
    magazine_price = models.IntegerField()

    def __str__(self):
        return self.magazine_name


    
        