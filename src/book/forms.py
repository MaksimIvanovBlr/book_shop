from django import forms
from django.core.exceptions import ValidationError
from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'
