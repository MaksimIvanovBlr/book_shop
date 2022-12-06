from django import forms
from . import models

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ('name','telefon_number','email_adress', 'adress','additional_information')


class StaffOrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ('status', 'name','telefon_number','email_adress', 'adress','additional_information')
# class AddBookInCartForm(forms.ModelForm):
#     class Meta:
#         model = models.BookInCart 
#         fields = ('cart','book','quantity',)
