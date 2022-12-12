from django import forms
from django.core.exceptions import ValidationError
from . import models


class ExchangeRateForm(forms.ModelForm):
    class Meta:
        model = models.ExchangeRate
        fields = ('rate',)
