from django.urls import path
from . import views 
app_name = 'comments'
urlpatterns = [
    path('delete-comment-book/<int:pk>', views.DeleteCommentBook.as_view(), name='delete-comment-book'),
    path('delete-comment-order/<int:pk>', views.DeleteCommentOrder.as_view(), name='delete-comment-order')
]