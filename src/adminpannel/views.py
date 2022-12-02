from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from book import models, forms 
from django.contrib.auth.models import User


class AdminPannel(PermissionRequiredMixin ,LoginRequiredMixin, generic.TemplateView):
    template_name = 'adminpannel/adminpannel.html'
    permission_required = ('book.change_book', 'auth.change_user')
    login_url = reverse_lazy('login')


class AdminPannelBook(PermissionRequiredMixin ,LoginRequiredMixin, generic.TemplateView):
    template_name = 'adminpannel/book.html'
    permission_required = ('book.change_book', 'auth.change_user')
    login_url = reverse_lazy('login')

class UserPannel(LoginRequiredMixin, generic.TemplateView):
    template_name = 'adminpannel/users.html'
    login_url = reverse_lazy('login')
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        u_id = self.request.user
        user_pk = User.objects.get(pk=u_id.pk)
        context['pk'] = user_pk.pk
        print('.!!!!!!!!!!!!!!!', user_pk)
        # context['user_url']= "{% url 'custom_user:detail-user' pk={{f'{id}'}} %}"
        return context   

