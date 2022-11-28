from django.urls import path
from . import views as ap_view
app_name = 'adminportal'
urlpatterns = [
 path(" ", ap_view.AdminPannel.as_view(), name="adminpannel"),
 path("book/", ap_view.AdminPannelBook.as_view(), name="book")
]