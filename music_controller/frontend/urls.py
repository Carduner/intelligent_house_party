from django.urls import path
from .views import index

app_name = 'frontend' # for redirect for spotify views

urlpatterns = [
    path('', index, name=''), # for redirect in spotify views
    path('join', index),
    path('create', index),
    path('room/<str:roomCode>', index)
]