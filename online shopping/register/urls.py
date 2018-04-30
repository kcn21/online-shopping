from django.urls import path
from django.conf.urls import url
from .import views
urlpatterns = [
# path('', views.index, name='index'),
    url(r'^index/$', views.index),
    url(r'^welcome/$',views.welcome),
    url(r'^getuserinfo/$', views.getuserinfo),
]
