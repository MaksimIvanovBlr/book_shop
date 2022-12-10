from django.urls import path
from . import views as b_views
app_name = 'book'
urlpatterns = [
    path('add-book/', b_views.AddBook.as_view(), name='add-book'),
    path('book/<int:pk>', b_views.DetailBook.as_view(), name='detail-book'),
    path('update-book/<int:pk>', b_views.UpdateBook.as_view(), name='update-book'),
    path('delete-book/<int:pk>', b_views.DeleteBook.as_view(), name='delete-book'),
    path('list-book/', b_views.ListBook.as_view(), name='list-book'),
    path('import-list-book/', b_views.book_list_import, name='import-list-book'),
    path('export-list-book/', b_views.book_list_export, name='export-list-book')

]