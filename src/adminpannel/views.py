from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from book import models, forms 


class AdminPannel(PermissionRequiredMixin ,LoginRequiredMixin, generic.TemplateView):
    template_name = 'adminpannel/adminpannel.html'
    permission_required = ('book.change_book', 'auth.change_user')
    login_url = reverse_lazy('login')
