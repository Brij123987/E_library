from django.db import models

# Create your models here.

class Newspaper(models.Model):
    prod_code = models.IntegerField(default=100)
    for_user = models.CharField(max_length=100, 
                              default='xyz'
                              )
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=500)
    item_price = models.IntegerField()
    item_image = models.CharField(
                                    max_length=500,
                                    default="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Placeholder_book.svg/1200px-Placeholder_book.svg.png"
                                    )

    def __str__(self):
        return self.item_name

class Comic(models.Model):
    prod_code = models.IntegerField(default=100)
    for_user = models.CharField(max_length=100, 
                              default='xyz'
                              )
    comic_name = models.CharField(max_length=50)
    comic_desc = models.CharField(max_length=500)
    comic_price = models.IntegerField()
    comic_image = models.CharField(
                                    max_length=500,
                                    default="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Placeholder_book.svg/1200px-Placeholder_book.svg.png"
                                    )

    def __str__(self):
        return self.comic_name

class Magazine(models.Model):
    prod_code = models.IntegerField(default=100)
    for_user = models.CharField(max_length=100, 
                              default='xyz'
                              )
    magazine_name = models.CharField(max_length=50)
    magazine_desc = models.CharField(max_length=500)
    magazine_price = models.IntegerField()
    magazine_image = models.CharField(
                                    max_length=500,
                                    default="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Placeholder_book.svg/1200px-Placeholder_book.svg.png"
                                    )

    def __str__(self):
        return self.magazine_name

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.email

        

class ELibraryModels(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdf')

    class Meta:
        ordering: ['title']

    def __str__(self):
        return self.title
        