from django.urls import path
from . import views as g_views
app_name = 'guide'

urlpatterns = [
    path('add-author/', g_views.AddAuthor.as_view(), name='add-author'),
    path('author/<int:pk>', g_views.DetailAuthor.as_view(), name='detail-author'),
    path('update-author/<int:pk>', g_views.UpdateAuthor.as_view(), name='update-author'),
    path('delete-author/<int:pk>', g_views.DeleteAuthor.as_view(), name='delete-author'),
    path('list-author/', g_views.ListAuthor.as_view(), name='list-author'),

    path('add-genre/', g_views.AddGenre.as_view(), name='add-genre'),
    path('genre/<int:pk>', g_views.DetailGenre.as_view(), name='detail-genre'),
    path('update-genre/<int:pk>', g_views.UpdateGenre.as_view(), name='update-genre'),
    path('delete-genre/<int:pk>', g_views.DeleteGenre.as_view(), name='delete-genre'),
    path('list-genre/', g_views.ListGenre.as_view(), name='list-genre'),

    path('add-series/', g_views.AddSeries.as_view(), name='add-series'),
    path('series/<int:pk>', g_views.DetailSeries.as_view(), name='detail-series'),
    path('update-series/<int:pk>', g_views.UpdateSeries.as_view(), name='update-series'),
    path('delete-series/<int:pk>', g_views.DeleteSeries.as_view(), name='delete-series'),
    path('list-series/', g_views.ListSeries.as_view(), name='list-series'),

    path('add-publishing/', g_views.AddPublishing.as_view(), name='add-publishing'),
    path('publishing/<int:pk>', g_views.DetailPublishing.as_view(), name='detail-publishing'),
    path('update-publishing/<int:pk>', g_views.UpdatePublishing.as_view(), name='update-publishing'),
    path('delete-publishing/<int:pk>', g_views.DeletePublishing.as_view(), name='delete-publishing'),
    path('list-publishing/', g_views.ListPublishing.as_view(), name='list-publishing')
]