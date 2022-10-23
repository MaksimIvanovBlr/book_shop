from dataclasses import fields
from django import forms
from django.core.exceptions import ValidationError
from . import models

class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'