from django import forms
from .models import OSUser
from django.contrib.auth.models import User
class userForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model=User
		fields=("first_name","last_name","username","password","email")

class OSUserserForm(forms.ModelForm):
	class Meta:
		model=OSUser
		fields=("mobile",)
	