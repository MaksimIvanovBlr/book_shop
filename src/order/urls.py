from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path("cart/", views.cart_view, name='cart'),
    path("delete-position/<int:pk>/", views.DeletePosition.as_view(), name='delete-position'),
    path("make-an-order/", views.MakeAnOrder.as_view(), name='make-an-order'),
    path("success/", views.SuccessView.as_view(), name='success'),
    path("list-order/", views.ListOrder.as_view(), name='list-order'),

    path('detail-order/<int:pk>', views.DetailOrder.as_view(), name='detail-order'),
    path('update-order/<int:pk>', views.UpdateOrder.as_view(), name='update-order'),
    path('delete-order/<int:pk>', views.DeleteOrder.as_view(), name='delete-order'),
    path('staff-update-order/<int:pk>', views.StaffUpdateOrder.as_view(), name='staff-update-order'),
    path("user-list-order/", views.UserListOrder.as_view(), name='user-list-order'),
    path("status-order/<int:pk>", views.UpdateStatusOrder.as_view(), name='status-order')

]
