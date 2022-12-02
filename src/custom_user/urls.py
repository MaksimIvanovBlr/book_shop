from django.urls import path
from . import views 
app_name = 'custom_user'

urlpatterns = [
path("registration/", views.RegisterUser.as_view(), name='registration'),
path("create-user/", views.CreateUser.as_view(), name='create-user'),
path('list-user/', views.ListExtendUser.as_view(), name='list-user'),
path("detail-user/<int:pk>", views.DetailUser.as_view(), name='detail-user'),
path("delete-user/<int:pk>/", views.DeleteUser.as_view(), name='delete-user'),
path('update-user/<int:pk>', views.UpdateUser.as_view(), name='update-user'),
path('update-extenduser/<int:pk>', views.UpdateExtendUser.as_view(), name='update-extenduser'),

]