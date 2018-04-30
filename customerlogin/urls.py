from django.urls import path

from django.contrib.auth import views 
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^customerlogin/',views.customerlogin),
    url(r'^sitehome/',views.sitehome),
	url(r'^home/',views.home),
    url(r'^auth/', views.auth_view),
    url(r'^logout/', views.logout),
    url(r'^invalidlogin/',views.invalidlogin)
]
