from django import forms
from book.models import Newspaper
from book.models import Magazine
from book.models import Comic
from book.models import Contact
from book.models import TimesofIndia,HindustanTime, IndianExpress, IndiaToday
from book.models import UploadComic, UploadMagazine

class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = ['prod_code','for_user','item_name','item_desc','item_price','item_image']

class MagazineForm(forms.ModelForm):
    class Meta:
        model = Magazine
        fields = ['prod_code','for_user','magazine_name','magazine_desc','magazine_price','magazine_image','pdf_file']

class ComicForm(forms.ModelForm):
    class Meta:
        model = Comic
        fields = ['prod_code','for_user','comic_name','comic_desc','comic_price','comic_image']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email','subject','message']	

class UploadTimesofIndiaNewspaper(forms.ModelForm):
    class Meta:
        model = TimesofIndia
        fields = ('title','day','month','pdf')

class UploadHindustanNewspaper(forms.ModelForm):
    class Meta:
        model = HindustanTime
        fields = ('title','day','month','pdf')

class UploadIndianExpressNewspaper(forms.ModelForm):
    class Meta:
        model = IndianExpress
        fields = ('title','day','month','pdf')

class UploadIndiaTodayNewspaper(forms.ModelForm):
    class Meta:
        model = IndiaToday
        fields = ('title','day','month','pdf')

class UploadComicPdf(forms.ModelForm):
    class Meta:
        model = UploadComic
        fields = ('title_name','pdf')

class UploadMagazinePdf(forms.ModelForm):
    class Meta:
        model = UploadMagazine
        fields = ('title_name','pdf')