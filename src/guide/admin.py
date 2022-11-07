from django.contrib import admin
from . import models

admin.site.register(models.Author)
admin.site.register(models.Genre)
admin.site.register(models.Publishing)
admin.site.register(models.Series)