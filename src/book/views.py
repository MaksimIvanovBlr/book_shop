from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from comments import models as c_models
from comments import forms as c_forms
from django.views.generic.edit import FormMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from tablib import Dataset

from .resources import BookResource

from . import models, forms


# кинги:

class AddBook(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Book
    form_class = forms.BookForm
    permission_required = 'book.add_book'
    login_url = reverse_lazy('login')
    template_name = 'book/edit_book.html'
    success_url = reverse_lazy('book:list-book')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
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
        return reverse_lazy('book:detail-book', kwargs={'pk': self.get_object().pk})


class UpdateBook(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Book
    form_class = forms.BookForm
    permission_required = 'book.add_book'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('book:list-book')
    template_name = 'book/edit_book.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Редактировать данные о книге'
        return context


class DeleteBook(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Book
    permission_required = 'book.delete_book'
    login_url = reverse_lazy('login')
    template_name = 'book/delete_book.html'
    success_url = reverse_lazy('book:list-book')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Удалить книгу'
        context['alarm_message'] = 'Вы точно хотите удалить данную книгу?'
        return context


class ListBook(generic.ListView):
    model = models.Book
    template_name = 'book/list_book.html'


# импорт/экспорт списков книг

def book_list_export(request):
    if request.user.is_authenticated == request.user.is_staff:
        if request.method == 'POST':
            file_format = request.POST['file-format']
            book_resource = BookResource()
            dataset = book_resource.export()
            if file_format == 'CSV':
                response = HttpResponse(dataset.csv, content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
                return response
            elif file_format == 'JSON':
                response = HttpResponse(dataset.json, content_type='application/json')
                response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
                return response
            elif file_format == 'XLS (Excel)':
                response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
                return response

        return render(request, 'book/export_book.html')
    else:
        raise PermissionDenied()


def book_list_import(request):
    if request.user.is_authenticated == request.user.is_staff:
        if request.method == 'POST':
            file_format = request.POST['file-format']
            book_resource = BookResource()
            dataset = Dataset()
            new_book = request.FILES['importData']

            if file_format == 'CSV':
                imported_data = dataset.load(new_book.read().decode('utf-8'), format='csv')
                result = book_resource.import_data(dataset, dry_run=True)
            elif file_format == 'JSON':
                imported_data = dataset.load(new_book.read().decode('utf-8'), format='json')
                result = book_resource.import_data(dataset, dry_run=True)

            if not result.has_errors():
                book_resource.import_data(dataset, dry_run=False)

        return render(request, 'book/import_book.html')
    else:
        raise PermissionDenied()
