from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('callback/q', views.callback, name = 'callback')
]
