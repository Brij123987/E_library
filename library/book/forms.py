from django import forms
from book.models import Newspaper
from book.models import Magazine
from book.models import Comic
from book.models import Contact
from book.models import ELibraryModels

class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = ['prod_code','for_user','item_name','item_desc','item_price','item_image']

class MagazineForm(forms.ModelForm):
    class Meta:
        model = Magazine
        fields = ['prod_code','for_user','magazine_name','magazine_desc','magazine_price','magazine_image']

class ComicForm(forms.ModelForm):
    class Meta:
        model = Comic
        fields = ['prod_code','for_user','comic_name','comic_desc','comic_price','comic_image']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email','subject','message']	

class UploadBookForm(forms.ModelForm):
    class Meta:
        model = ELibraryModels
        fields = ('title','pdf')