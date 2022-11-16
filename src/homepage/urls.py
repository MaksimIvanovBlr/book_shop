from django.urls import path
from . import views as hp_view
app_name = 'homepage'

urlpatterns = [
path("", hp_view.HomePage.as_view(), name='home'),
path("search/", hp_view.SearchResults.as_view(), name='search')
]