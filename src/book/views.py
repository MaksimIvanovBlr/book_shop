from django.shortcuts import render

from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy

from . import models, forms

# кинги:

class AddBook(generic.CreateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'book/edit_book.html'
    success_url = reverse_lazy('book:list-book')
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Добавить книгу'
        return context    

class DetailBook(generic.DetailView):
    model = models.Book
    template_name = 'book/detail_book.html'

class UpdateBook(generic.UpdateView):
    model = models.Book
    form_class = forms.BookForm
    success_url = reverse_lazy('book:list-book')
    template_name = 'book/edit_book.html'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Редактировать данные о книге'
        return context

class DeleteBook(generic.DeleteView):
    model = models.Book
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

