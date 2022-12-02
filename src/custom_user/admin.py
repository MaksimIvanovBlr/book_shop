from django.contrib import admin
from . import models

class ExtendUserAdmin(admin.ModelAdmin):
    list_display = ('extend_user','phone','country','city','index','adress1','adress2')

admin.site.register(models.ExtendUser, ExtendUserAdmin)

# Register your models here.
