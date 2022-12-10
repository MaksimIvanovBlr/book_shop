from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from . import models, forms


# авторы:

class AddAuthor(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Author
    form_class = forms.AuthorForm
    permission_required = 'guide.add_author'
    login_url = reverse_lazy('login')
    template_name = 'guide/edit_guide.html'
    success_url = reverse_lazy('guide:list-author')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Добавить автора'
        return context


class DetailAuthor(generic.DetailView):
    model = models.Author
    template_name = 'guide/detail_author.html'


class UpdateAuthor(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Author
    form_class = forms.AuthorForm
    permission_required = 'guide.add_author'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('guide:list-author')
    template_name = 'guide/edit_guide.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Редактировать данные автора'
        return context


class DeleteAuthor(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Author
    login_url = reverse_lazy('login')
    permission_required = 'guide.add_author'
    template_name = 'guide/delete_guide.html'
    success_url = reverse_lazy('guide:list-author')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Удалить автора'
        context['alarm_message'] = 'Вы точно хотите удалить данного автора?'
        return context


class ListAuthor(generic.ListView):
    model = models.Author
    template_name = 'guide/list_author.html'


# жанры:

class AddGenre(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Genre
    form_class = forms.GenreForm
    permission_required = 'guide.add_genre'
    login_url = reverse_lazy('login')
    template_name = 'guide/edit_guide.html'
    success_url = reverse_lazy('guide:list-genre')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Добавить жанр'
        return context


class DetailGenre(generic.DetailView):
    model = models.Genre
    template_name = 'guide/detail_guide.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Описание жанра'
        context['some_list'] = 'object.genrebook.all'
        detail = self.get_object()
        print(detail)
        print(detail.genrebook.all())
        return context


class UpdateGenre(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Genre
    form_class = forms.GenreForm
    permission_required = 'guide.add_genre'
    login_url = reverse_lazy('login')
    template_name = 'guide/edit_guide.html'
    success_url = reverse_lazy('guide:list-genre')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Редактировать жанр'
        return context


class DeleteGenre(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Genre
    permission_required = 'guide.add_genre'
    login_url = reverse_lazy('login')
    template_name = 'guide/delete_guide.html'
    success_url = reverse_lazy('guide:list-genre')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Удалить жанр'
        context['alarm_message'] = 'Вы точно хотите удалить данный жанр?'
        context['url_delete'] = "{% url 'guide:delete-genre' pk=obj.pk %}"
        return context


class ListGenre(generic.ListView):
    model = models.Genre
    template_name = 'guide/list_guide.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Жанры'
        context['update'] = 'guide:update-genre'
        context['delete'] = 'guide:delete-genre'
        context['detail'] = 'guide:detail-genre'
        return context

    # серии


class AddSeries(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Series
    form_class = forms.SeriesForm
    permission_required = 'guide.add_series'
    login_url = reverse_lazy('login')
    template_name = 'guide/edit_guide.html'
    success_url = reverse_lazy('guide:list-series')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Добавить серию'
        return context


class DetailSeries(generic.DetailView):
    model = models.Series
    template_name = 'guide/detail_series.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Данные о серии'
        return context


class UpdateSeries(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Series
    form_class = forms.SeriesForm
    permission_required = 'guide.add_series'
    login_url = reverse_lazy('login')
    template_name = 'guide/edit_guide.html'
    success_url = reverse_lazy('guide:list-series')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Редактировать серию'
        return context


class DeleteSeries(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Series
    permission_required = 'guide.add_series'
    login_url = reverse_lazy('login')
    template_name = 'guide/delete_guide.html'
    success_url = reverse_lazy('guide:list-series')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Удалить серию'
        context['alarm_message'] = 'Вы точно хотите удалить данную серию?'
        return context


class ListSeries(generic.ListView):
    model = models.Series
    template_name = 'guide/list_guide.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Серии'
        context['update'] = 'guide:update-series'
        context['delete'] = 'guide:delete-series'
        context['detail'] = 'guide:detail-series'
        return context

    # издательство


class AddPublishing(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Publishing
    form_class = forms.PublishingForm
    permission_required = 'guide.add_publishing'
    login_url = reverse_lazy('login')
    template_name = 'guide/edit_guide.html'
    success_url = reverse_lazy('guide:list-publishing')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Добавить издательство'
        return context


class DetailPublishing(generic.DetailView):
    model = models.Publishing
    template_name = 'guide/detail_publishing.html'


class UpdatePublishing(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Publishing
    form_class = forms.PublishingForm
    permission_required = 'guide.add_publishing'
    login_url = reverse_lazy('login')
    template_name = 'guide/edit_guide.html'
    success_url = reverse_lazy('guide:list-publishing')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Редактировать издательство'
        return context


class DeletePublishing(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Publishing
    permission_required = 'guide.add_publishing'
    login_url = reverse_lazy('login')
    template_name = 'guide/delete_guide.html'
    success_url = reverse_lazy('guide:list-publishing')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Удалить издательство'
        context['alarm_message'] = 'Вы точно хотите удалить данное издательство?'
        return context


class ListPublishing(generic.ListView):
    model = models.Publishing
    template_name = 'guide/list_guide.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Издательства'
        context['update'] = 'guide:update-publishing'
        context['delete'] = 'guide:delete-publishing'
        context['detail'] = 'guide:detail-publishing'
        return context
