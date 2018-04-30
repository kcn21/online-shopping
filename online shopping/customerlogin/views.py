from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def customerlogin(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('loginuser.html', c)


def auth_view(request):
   # if request.method=="POST":
	username = request.POST.get('uname', '')
	password = request.POST.get('pwd', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/customerlogin/sitehome/')
	return HttpResponseRedirect('/customerlogin/invalidlogin/')

@login_required(login_url='/customerlogin/customerlogin/')
def sitehome(request):
	c = {}
	c.update(csrf(request))
	c['full_name']=request.user.username
	return render(request,'sitehome.html', c)

#@login_required(login_url='/customerlogin/customerlogin/')
def home(request):
	
	c = {}
	return render_to_response('home2.html',c)

@login_required(login_url='/customerlogin/customerlogin/')
def invalidlogin(request):
	c = {}
	c['error']="invalidlogin please login again"
	return render(request,'loginuser.html',c)

@login_required(login_url='/customerlogin/customerlogin/')
def logout(request):
    auth.logout(request)
    return render(request,"userlogout.html")