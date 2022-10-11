from django.contrib import admin
from . import models

admin.site.register(models.Author)
admin.site.register(models.Genre)
admin.site.register(models.Publishing)
admin.site.register(models.Series)
admin.site.register(models.Restrictions)
admin.site.register(models.Format)
admin.site.register(models.Binding)

