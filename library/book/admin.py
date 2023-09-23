from django.contrib import admin
from book.models import Newspaper
from book.models import Comic
from book.models import Magazine


# Register your models here.

admin.site.register(Newspaper)
admin.site.register(Comic)
admin.site.register(Magazine)
