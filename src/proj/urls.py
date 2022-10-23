"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from guide import views as g_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('add-author/', g_views.AddAuthor.as_view()),
    path('author/<int:pk>', g_views.DetailAuthor.as_view()),
    path('update-author/<int:pk>', g_views.UpdateAuthor.as_view()),
    path('delete-author/<int:pk>', g_views.DeleteAuthor.as_view()),
    path('list-author/', g_views.ListAuthor.as_view())

]
