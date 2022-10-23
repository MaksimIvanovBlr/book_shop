from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

import datetime
from . import models, forms

class AddAuthor(generic.CreateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'guide/add_author.html'

class DetailAuthor(generic.DetailView):
    model = models.Author
    template_name = 'guide/detail_author.html'

class UpdateAuthor(generic.UpdateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'guide/update_author.html'

class DeleteAuthor(generic.DeleteView):
    model = models.Author
    template_name = 'guide/delete_author.html'
    def get_success_url(self):
        return '/list-author'

class ListAuthor(generic.ListView):
    model = models.Author
    template_name = 'guide/list_author.html'