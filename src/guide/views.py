from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy

import datetime
from . import models, forms

# авторы:

class AddAuthor(generic.CreateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'guide/edit_guide.html'
    success_url = reverse_lazy('guide:list-author')
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Добавить автора'
        return context    

class DetailAuthor(generic.DetailView):
    model = models.Author
    template_name = 'guide/detail_author.html'

class UpdateAuthor(generic.UpdateView):
    model = models.Author
    form_class = forms.AuthorForm
    success_url = reverse_lazy('guide:list-author')
    template_name = 'guide/edit_guide.html'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Редактировать данные автора'
        return context

class DeleteAuthor(generic.DeleteView):
    model = models.Author
    template_name = 'guide/delete_guide.html'
    success_url = reverse_lazy('guide:list-author')
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Удалить автора'
        context['alarm_message'] = 'Вы точно хотите удалить данного автора?'
        return context

class ListAuthor(generic.ListView):
    model = models.Author
    template_name = 'guide/list_author.html'


# жанры:

class AddGenre(generic.CreateView):
    model = models.Genre
    form_class = forms.GenreForm
    template_name = 'guide/edit_guide.html'
    success_url = reverse_lazy('guide:list-genre')
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Добавить жанр'
        return context     

class DetailGenre(generic.DetailView):
    model = models.Genre
    template_name = 'guide/detail_guide.html'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Описание жанра'
        return context    

class UpdateGenre(generic.UpdateView):
    model = models.Genre
    form_class = forms.GenreForm
    template_name = 'guide/edit_guide.html'
    success_url = reverse_lazy('guide:list-genre')
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Редактировать жанр'
        return context     

class DeleteGenre(generic.DeleteView):
    model = models.Genre
    template_name = 'guide/delete_guide.html'
    success_url = reverse_lazy('guide:list-genre')
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Удалить жанр'
        context['alarm_message'] = 'Вы точно хотите удалить данный жанр?'
        context['url_delete'] = "{% url 'guide:delete-genre' pk=obj.pk %}"
        return context

class ListGenre(generic.ListView):
    model = models.Genre
    template_name = 'guide/list_guide.html'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Жанры'
        context['update'] = 'guide:update-genre'
        context['delete'] = 'guide:delete-genre'
        return context  

# серии

class AddSeries(generic.CreateView):
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'guide/edit_guide.html'
    success_url = reverse_lazy('guide:list-series')
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Добавить серию'
        return context     

class DetailSeries(generic.DetailView):
    model = models.Series
    template_name = 'guide/detail_guide.html'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Данные о серии'
        return context    

class UpdateSeries(generic.UpdateView):
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'guide/edit_guide.html'
    success_url = reverse_lazy('guide:list-series')
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Редактировать серию'
        return context     

class DeleteSeries(generic.DeleteView):
    model = models.Series
    template_name = 'guide/delete_guide.html'
    success_url = reverse_lazy('guide:list-series')
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Удалить серию'
        context['alarm_message'] = 'Вы точно хотите удалить данную серию?'
        return context  

class ListSeries(generic.ListView):
    model = models.Series
    template_name = 'guide/list_guide.html'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Серии'
        context['update'] = 'guide:update-series'
        context['delete'] = 'guide:delete-series'
        return context  


# издательство

class AddPublishing(generic.CreateView):
    model = models.Publishing
    form_class = forms.PublishingForm
    template_name = 'guide/edit_guide.html'
    success_url = reverse_lazy('guide:list-publishing')
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Добавить издательство'
        return context     

class DetailPublishing(generic.DetailView):
    model = models.Publishing
    template_name = 'guide/detail_publishing.html'

class UpdatePublishing(generic.UpdateView):
    model = models.Publishing
    form_class = forms.PublishingForm
    template_name = 'guide/edit_guide.html'
    success_url = reverse_lazy('guide:list-publishing')
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Редактировать издательство'
        return context     

class DeletePublishing(generic.DeleteView):
    model = models.Publishing
    template_name = 'guide/delete_guide.html'
    success_url = reverse_lazy('guide:list-publishing')
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Удалить издательство'
        context['alarm_message'] = 'Вы точно хотите удалить данное издательство?'
        return context 

class ListPublishing(generic.ListView):
    model = models.Publishing
    template_name = 'guide/list_guide.html'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Издательства'
        context['update'] = 'guide:update-publishing'
        context['delete'] = 'guide:delete-publishing'
        return context  
