from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from book import models, forms 
from django.db.models import Q


class HomePage(generic.TemplateView):
    template_name = 'homepage/homepage.html'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['book'] = models.Book.objects.all().order_by('-id')[:5]
        context['total_quantiti_in_cart'] = '888'
        return context 

class SearchResults(generic.ListView):
    model = models.Book
    template_name = 'homepage/search.html'
    # queryset = models.Book.objects.filter(name__icontains='Билли')
    def get_queryset(self): 
        query = self.request.GET.get('tosearch')
        object_list = models.Book.objects.filter(Q(name__icontains=query))
        return object_list