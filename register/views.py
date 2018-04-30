from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf 
from register.models import OSUser
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from . import forms
from .models import OSUser

def getuserinfo(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('register.html', c)

def index(request):
	c = {}
	c.update(csrf(request))
	f_name=request.POST.get('fname','')
	uname = request.POST.get('username','')
	l_name = request.POST.get('lname','')
	pwd=request.POST.get('pwd','')
	cpwd = request.POST.get('cpwd','')
	emailid=request.POST.get('emailid','')
	mobilen=request.POST.get('mobile','')
	if User.objects.filter(username=uname).exists()==True:
		return render_to_response('register.html', {"error3": "username already exist"})
		
	else:
		if pwd==cpwd:
			if len(pwd)>=8:
				s=User.objects.create_user(username=uname,password=pwd,email=emailid,first_name=f_name,last_name=l_name)
				print(s)
				s.OSUser=OSUser(user=s,mobile=mobilen)
				s.save()
				s.OSUser.save()
				return HttpResponseRedirect('/customerlogin/customerlogin')
			else:
				return render_to_response('register.html',{"error1":"password length is less than 8"})

		return render_to_response('register.html', {"error2": "password doesn't match enter again"})

def welcome(request): 
    return HttpResponse("you're registered.:)")







