
from django import forms
from . import models



class CommentToBookForm(forms.ModelForm):
    class Meta:
        model = models.CommentToBook
        fields = ('message',)

class CommentToOrderForm(forms.ModelForm):
    class Meta:
        model = models.CommentToOrder
        fields = ('message',)
