from django.urls import path
from django.conf.urls import url, include
from . import views
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signin', views.signin, name = 'signin'),
    path('callback/q', views.callback, name = 'callback'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
