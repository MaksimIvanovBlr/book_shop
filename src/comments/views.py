from . import models
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class DeleteCommentBook(UserPassesTestMixin, LoginRequiredMixin, generic.DeleteView):
    model = models.CommentToBook
    login_url = reverse_lazy('login')
    template_name = 'comments/delete_comment.html'
    success_url = reverse_lazy('book:list-book')
    def test_func(self):
        if self.request.user.is_authenticated != self.request.user.is_staff:
            detail = self.get_object()
            if self.request.user == detail.author:
                return True
            return False
        else:
            return True

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Удалить комментарий к книге'
        context['alarm_message'] = 'Вы точно хотите удалить данный комментарий?'
        return context

class DeleteCommentOrder(UserPassesTestMixin, LoginRequiredMixin, generic.DeleteView):
    model = models.CommentToOrder
    login_url = reverse_lazy('login')
    template_name = 'comments/delete_comment.html'
    success_url = reverse_lazy('adminportal:userpannel')
    def test_func(self):
        if self.request.user.is_authenticated != self.request.user.is_staff:
            detail = self.get_object()
            if self.request.user == detail.author:
                return True
            return False
        else:
            return True
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['operation'] = 'Удалить комментарий к заказу'
        context['alarm_message'] = 'Вы точно хотите удалить данный комментарий?'
        return context