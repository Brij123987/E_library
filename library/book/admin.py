from django.contrib import admin
from book.models import Newspaper
from book.models import Comic
from book.models import Magazine
from book.models import Contact
from book.models import TimesofIndia,HindustanTime, IndianExpress, IndiaToday


# Register your models here.

admin.site.register(Newspaper)
admin.site.register(Comic)
admin.site.register(Magazine)
admin.site.register(Contact)
admin.site.register(TimesofIndia)
admin.site.register(HindustanTime)
admin.site.register(IndianExpress)
admin.site.register(IndiaToday)
