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

class ChangeOrderStatusForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(ChangeOrderStatusForm, self).__init__(*args, **kwargs)
            if self.instance:
                self.fields['status'].queryset = models.Statuses.objects.filter(status='Отменен')
    class Meta:
        model = models.Order
        fields = ('status', )
