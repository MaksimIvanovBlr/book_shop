from dataclasses import fields
from django import forms
from django.core.exceptions import ValidationError
from . import models


class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'


class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = '__all__'


class SeriesForm(forms.ModelForm):
    class Meta:
        model = models.Series
        fields = '__all__'


class PublishingForm(forms.ModelForm):
    class Meta:
        model = models.Publishing
        fields = '__all__'
