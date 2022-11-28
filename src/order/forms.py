from django import forms
from . import models

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ('name','telefon_number','email_adress', 'adress','additional_information')
