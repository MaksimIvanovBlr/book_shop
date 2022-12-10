from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from . import models, forms
from django.contrib.auth.models import User, Group


class CreateUser(LoginRequiredMixin, generic.CreateView):
    model = models.ExtendUser
    form_class = forms.ExtendUserForm
    template_name = 'custom_user/create_user.html'
    success_url = reverse_lazy('homepage:home')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        u_id = self.request.user
        form.instance.extend_user = User.objects.get(pk=u_id.pk)
        return super().form_valid(form)

    def get_success_url(self):
        group_to_add = Group.objects.get(name='Customers')
        group_to_add.user_set.add(self.request.user)
        return super().get_success_url()


class RegisterUser(generic.CreateView):
    form_class = forms.RegisterUserForm
    template_name = 'custom_user/register_user.html'
    success_url = reverse_lazy('custom_user:create-user')


class ListExtendUser(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = User
    permission_required = ('book.change_book', 'auth.change_user')
    template_name = 'custom_user/list_user.html'
    login_url = reverse_lazy('login')


class DetailUser(UserPassesTestMixin, generic.DetailView):
    model = User
    template_name = 'custom_user/detail_user.html'

    def test_func(self):
        if self.request.user.is_authenticated != self.request.user.is_staff:
            detail = self.get_object()
            if self.request.user == detail:
                return True
            return False
        else:
            return True


class UpdateUser(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = forms.RegisterUserForm
    login_url = reverse_lazy('login')
    if User.is_staff:
        success_url = reverse_lazy('custom_user:list-user')
    else:
        success_url = reverse_lazy('adminportal:userportal')
    template_name = 'custom_user/edit_user.html'

    def form_valid(self, form):
        extenduser, created = models.ExtendUser.objects.get_or_create(
            extend_user=self.request.user,
            defaults={
                'phone': 11111,
                'country': 'нет данных',
                'city': 'нет данных',
                'index': 11111,
                'adress1': 'нет данных',
                'information': 'нет данных',
            })
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_authenticated != self.request.user.is_staff:
            detail = self.get_object()
            if self.request.user == detail:
                return True
            return False
        else:
            return True

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pk'] = None
        return context


class UpdateExtendUser(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = models.ExtendUser
    form_class = forms.ExtendUserForm
    login_url = reverse_lazy('login')
    if User.is_staff:
        success_url = reverse_lazy('custom_user:list-user')
    else:
        success_url = reverse_lazy('homepage:home')

    template_name = 'custom_user/edit_extenduser.html'

    def test_func(self):
        if self.request.user.is_authenticated != self.request.user.is_staff:
            detail = self.get_object()
            if self.request.user.extenduser == detail:
                return True
            return False
        else:
            return True


class DeleteUser(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = User
    permission_required = 'auth.change_user'
    login_url = reverse_lazy('login')
    template_name = 'custom_user/delete_user.html'
    success_url = reverse_lazy('custom_user:list-user')
