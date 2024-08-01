from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
  path('list/', user_list, name='list'),
  path('create/', create, name='create'),
  path('delete/<int:pk>/', delete, name='delete'),
  path('update/<int:pk>/', update, name='update'),
]