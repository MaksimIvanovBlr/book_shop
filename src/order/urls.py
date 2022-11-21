from django.urls import path
from . import views 
app_name = 'order'

urlpatterns = [
path("cart/", views.cart_view, name='cart'),

]