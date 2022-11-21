from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . import models
from book import models as b_models

# class CartView(generic.TemplateView):
#     template_name  = 'order/cart.html'

def cart_view(request):
    context = {}
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
            cart,created = models.Cart.objects.get_or_create(
            pk=cart_id,
            defaults= {'user':user}
            )
            if created:
                request.session['cart_id'] = cart.pk
            
            book = b_models.Book.objects.get(pk = int(book_pk))
            # quantity =
            price  = book.price
            # print(price)

            book_in_cart = models.BookInCart.objects.create(
                book=book,
                cart=cart,
                quantity=quantity,
                price=price
            )
                        
    

    return render(
        request=request, 
        template_name='order/cart.html',

    )

