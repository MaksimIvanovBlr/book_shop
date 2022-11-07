from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy


class HomePage(generic.TemplateView):
    template_name = 'homepage/homepage.html'
