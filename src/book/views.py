from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from comments import models as c_models
from comments import forms as c_forms
from django.views.generic.edit import FormMixin

from . import models, forms

# кинги:

class AddBook(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Book
    form_class = forms.BookForm
    permission_required = 'book.add_book'
    login_url = reverse_lazy('login')
    template_name = 'book/edit_book.html'
    success_url = reverse_lazy('book:list-book')
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Добавить книгу'
        return context    

class DetailBook(FormMixin, generic.DetailView):
    model = models.Book
    template_name = 'book/detail_book.html'
    form_class = c_forms.CommentToBookForm
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        return self.form_valid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.book = self.get_object()
        form.save()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('book:detail-book', kwargs={'pk':self.get_object().pk})


class UpdateBook(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Book
    form_class = forms.BookForm
    permission_required = 'book.add_book'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('book:list-book')
    template_name = 'book/edit_book.html'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Редактировать данные о книге'
        return context

class DeleteBook(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Book
    permission_required = 'book.delete_book'
    login_url = reverse_lazy('login')
    template_name = 'book/delete_book.html'
    success_url = reverse_lazy('book:list-book')
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Удалить книгу'
        context['alarm_message'] = 'Вы точно хотите удалить данную книгу?'
        return context

class ListBook(generic.ListView):
    model = models.Book
    template_name = 'book/list_book.html'

