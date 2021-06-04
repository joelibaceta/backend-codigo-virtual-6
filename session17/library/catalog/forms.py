from catalog.models import Book, Author
from django import forms
from django.forms.models import ModelForm

# Formulario Generico
class BookForm(forms.Form):
    title = forms.CharField(label="Title: ")
    autor = forms.ModelChoiceField(queryset=Author.objects.all())
    editorial = forms.CharField(label="Editorial: ")
    year = forms.IntegerField(label="Year: ")
    volume = forms.IntegerField(label="Volume: ")

# Formularios de modelo
class ModelBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'editorial', 'author', 'year', 'volume']
