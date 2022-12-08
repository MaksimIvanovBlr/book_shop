from django.contrib import admin
from . import models
admin.site.register(models.CommentToBook)
admin.site.register(models.CommentToOrder)

