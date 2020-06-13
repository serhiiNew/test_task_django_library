from django import forms
from .models import Book, Author


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields =[
            'title',
            'author',
        ]


class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Author
        fields =[
            'name',
        ]