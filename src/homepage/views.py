from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy

from book import models, forms 


class HomePage(generic.TemplateView):
    template_name = 'homepage/homepage.html'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['book'] = 'cdf'
        return context    
