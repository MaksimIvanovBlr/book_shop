from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . import models, forms
from book import models as b_models
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.contrib.auth.models import User
from django.views.generic.edit import FormMixin
from comments import forms as c_forms
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q


def cart_view(request):
    context = {}
    context['cart'] = None
    if request.method == 'POST':
        book_pk = request.POST.get('book_pk')
        quantity = request.POST.get('quantity')

        if book_pk and quantity:
            cart_id = int(request.session.get('cart_id', 0))
            if cart_id == 0:
                cart_id = None
            if request.user.is_authenticated:
                user = request.user
                # print(user)
            else:
                user = None
            cart, created = models.Cart.objects.get_or_create(
                pk=cart_id,
                defaults={'user': user}
            )
            context['cart'] = cart
            if created:
                request.session['cart_id'] = cart.pk

            book = b_models.Book.objects.get(pk=int(book_pk))
            price = book.price

            book_in_cart, created = models.BookInCart.objects.get_or_create(
                book=book,
                cart=cart,
                defaults={
                    'quantity': quantity,
                    'price': price
                }
            )
            if not created:
                book_in_cart.quantity += int(quantity)
                book_in_cart.save()
    else:
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart = models.Cart.objects.get(pk=cart_id)
            context['cart'] = cart

    return render(
        request=request,
        template_name='order/cart.html',
        context=context

    )


class DeletePosition(UserPassesTestMixin, generic.DeleteView):
    model = models.BookInCart
    success_url = reverse_lazy('order:cart')
    template_name = 'order/delete_position.html'

    def test_func(self):
        if self.request.user.is_authenticated != self.request.user.is_staff:
            detail = self.get_object()
            if self.request.user == detail.cart.user:
                return True
            return False
        else:
            return True


class MakeAnOrder(generic.CreateView):
    model = models.Order
    template_name = 'order/create_order.html'
    form_class = forms.OrderForm
    success_url = reverse_lazy('order:success')

    def form_valid(self, form):
        cart = models.Cart.objects.get(pk=self.request.session.get('cart_id'))
        form.instance.cart = cart
        form.instance.status = models.Statuses.objects.get(pk=1)
        return super().form_valid(form)

    def get_success_url(self):
        del self.request.session['cart_id']
        # subject = 'Новый заказ'
        # message = 'Появился новый заказ!'
        # email_from = 'fortestsendingdjango@mail.ru'
        # recipient_list = ['someone736970@gmail.com', ]
        # send_mail( subject, message, email_from, recipient_list )
        return super().get_success_url()


class SuccessView(generic.TemplateView):
    model = models.Order
    template_name = 'order/success_order.html'
    print(model.name)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(models.Order.objects.get(self.request.session.get(pk=10)))
        # context['order'] = models.Order.objects.get()
        # last_order = models.Order.objects.all().order_by('-id')[:1]
        # print(last_order.name )
        # context['order'] = last_order
        return context


class ListOrder(PermissionRequiredMixin, LoginRequiredMixin, generic.ListView):
    model = models.Order
    permission_required = ('book.change_book', 'auth.change_user')
    template_name = 'order/list_order.html'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return super(ListOrder, self).get_queryset().order_by('-updated_date')


class UserListOrder(LoginRequiredMixin, generic.ListView):
    model = models.Cart
    template_name = 'order/user_list_order.html'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        user_1 = self.request.user
        mod = models.Cart.objects.all()
        user_2 = self.request.user.user_cart.all()
        print('!!!!!!!!!!!!!!!!!', user_1, mod, user_2)
        object_list = models.Cart.objects.filter(user=user_1)
        return object_list


class DetailOrder(FormMixin, UserPassesTestMixin, LoginRequiredMixin, generic.DetailView):
    model = models.Order
    template_name = 'order/detail_order.html'
    login_url = reverse_lazy('login')
    form_class = c_forms.CommentToOrderForm

    def test_func(self):
        if self.request.user.is_authenticated != self.request.user.is_staff:
            detail = self.get_object()
            if self.request.user == detail.cart.user:
                return True
            return False
        else:
            return True

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        return self.form_valid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.order = self.get_object()
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('order:detail-order', kwargs={'pk': self.get_object().pk})


class UpdateOrder(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = models.Order
    form_class = forms.OrderForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('order:list-order')
    template_name = 'order/edit_order.html'

    def test_func(self):
        if self.request.user.is_authenticated != self.request.user.is_staff:
            detail = self.get_object()
            if self.request.user == detail.cart.user:
                return True
            return False
        else:
            return True


class DeleteOrder(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Order
    permission_required = 'book.delete_book'
    login_url = reverse_lazy('login')
    template_name = 'order/delete_order.html'
    success_url = reverse_lazy('order:list-order')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Удалить заказ'
        context['alarm_message'] = 'Вы точно хотите удалить данный заказ?'
        return context


class StaffUpdateOrder(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Order
    form_class = forms.StaffOrderForm
    permission_required = 'book.add_book'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('order:list-order')
    template_name = 'order/staff_edit_order.html'


class UpdateStatusOrder(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = models.Order
    form_class = forms.ChangeOrderStatusForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('order:list-order')
    template_name = 'order/status_order.html'

    def test_func(self):
        if self.request.user.is_authenticated != self.request.user.is_staff:
            detail = self.get_object()
            if self.request.user == detail.cart.user:
                return True
            return False
        else:
            return True
