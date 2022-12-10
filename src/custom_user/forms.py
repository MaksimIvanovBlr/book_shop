from dataclasses import fields
from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')


class ExtendUserForm(forms.ModelForm):
    class Meta:
        model = models.ExtendUser
        fields = ('phone', 'country', 'city', 'index', 'adress1', 'adress2', 'information')
