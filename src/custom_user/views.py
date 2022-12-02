from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models, forms
from django.contrib.auth.models import User


class CreateUser(LoginRequiredMixin, generic.CreateView):
    model = models.ExtendUser
    form_class = forms.ExtendUserForm
    template_name = 'custom_user/create_user.html'
    success_url = reverse_lazy('homepage:home')
    login_url = reverse_lazy('login')   
    def form_valid(self,form):
        u_id = self.request.user
        form.instance.extend_user = User.objects.get(pk=u_id.pk)
        return super().form_valid(form)

class RegisterUser(generic.CreateView):
    form_class = forms.RegisterUserForm
    template_name = 'custom_user/register_user.html'
    success_url = reverse_lazy('custom_user:create-user')



class ListExtendUser(PermissionRequiredMixin, LoginRequiredMixin, generic.ListView):
    model = User
    permission_required = ('book.change_book', 'auth.change_user')
    template_name = 'custom_user/list_user.html'
    login_url = reverse_lazy('login')



class DetailUser(generic.DetailView):
    model = User
    template_name = 'custom_user/detail_user.html'

class UpdateUser(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = User
    form_class = forms.RegisterUserForm
    permission_required = 'auth.change_user'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('custom_user:list-user')
    template_name = 'custom_user/edit_user.html'

class UpdateExtendUser(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = User
    form_class = forms.ExtendUserForm
    permission_required = 'auth.change_user'
    login_url = reverse_lazy('login')
    if User.is_staff:
        success_url = reverse_lazy('custom_user:list-user')
    else:
        success_url = reverse_lazy('homepage:home')
    
    template_name = 'custom_user/edit_extenduser.html'

class DeleteUser(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = User
    permission_required = 'auth.change_user'
    login_url = reverse_lazy('login')
    template_name = 'custom_user/delete_user.html'
    success_url = reverse_lazy('custom_user:list-user')
