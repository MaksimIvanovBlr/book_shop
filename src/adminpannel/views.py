from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy

from book import models, forms 


class AdminPannel(generic.TemplateView):
    template_name = 'adminpannel/adminpannel.html'
