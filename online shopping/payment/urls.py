from django.conf.urls import url
from . import views 
#from django.contrib.auth import views
#from django.urls import path

urlpatterns=[
	url(r'^product/',views.product),
	#url(r'^cart/',views.cart),

	
]