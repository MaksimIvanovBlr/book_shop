from django.contrib import admin
from . import models


class CartAdmin(admin.ModelAdmin):
    list_display = ('pk','user')

class BookInCartAdmin(admin.ModelAdmin):
    list_display = ('pk','book','cart','quantity','price','created_date','update_date')


admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.BookInCart, BookInCartAdmin)
admin.site.register(models.Statuses)
admin.site.register(models.Order)
