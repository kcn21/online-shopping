from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from .models import stock
from django.contrib.auth.models import User

@login_required(login_url='/customerlogin/customerlogin/')
def product(request):
	c={}
	c.update(csrf(request))
		
	qty1=request.POST.get('q1')
	qty2=request.POST.get('q2')
	qty3=request.POST.get('q3')
	qty4=request.POST.get('q4')
	phone1=request.POST.get('phone1')
	phone2=request.POST.get('phone2')
	phone3=request.POST.get('phone3')
	phone4=request.POST.get('phone4')
	qty = {}
			
	request.session['qty'] = qty
	var = request.session['qty']
	total=0
	if phone1 == str('on'):
		qty['iPhone X'] = int(qty1)*100000
		total=total+qty['iPhone X']
		'''add=stock(user=request.user ,itemstock=qty1 ,itemcost=(int(qty1)*100000),itemname="iPhone X")
		add.save()'''
		#print(add.itemcost)
	#print(add)
	if phone2 == str('on'):
		qty['Samsung Galaxy'] = int(qty2)*50000
		total=total+qty['Samsung Galaxy']
		'''add=stock(user=request.user ,itemstock=qty2 ,itemcost=(int(qty2)*50000),itemname="Samsung Galaxy")
		add.save()'''
	if phone3 == str('on'):
		qty['Nexus'] = int(qty3)*35000
		total=total+qty['Nexus']
		'''add=stock(user=request.user ,itemstock=qty3 ,itemcost=(int(qty3)*35000),itemname="nexus")
		add.save()'''
	if phone4 == str('on'):
		qty['iPhone 7'] = int(qty4)*50000
		total=total+qty['iPhone 7']
		'''add=stock(user=request.user ,itemstock=qty4 ,itemcost=(int(qty4)*50000),itemname="iPhone 7")
		add.save()'''
	
	c['item']=var
	c['total']=total
	
	
		
	#items=[]
	#p=request.POST.get('id1','')
	
	#c['items']=stock.objects.filter(user=request.user) 

	return render(request,'product.html',c)
	
#def bill(request):

	