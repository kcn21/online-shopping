from django.conf.urls import url,include 
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^hello_world/', include('hello_world.urls')),
    url(r'^firstdbtest/',include('firstdbtest.urls')),
	url(r'^register/',include('register.urls')),
	url(r'^customerlogin/',include('customerlogin.urls')),
	url(r'^payment/',include('payment.urls'))
]


