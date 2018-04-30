from django.db import models
from django.contrib.auth.models import User


#from django.contrib.auth.models import User
class stock(models.Model):
	user= models.ForeignKey(User,on_delete=models.CASCADE)
	#username=models.CharField(max_length=100,required)
	itemstock=models.PositiveIntegerField()
	itemcost=models.PositiveIntegerField()
	itemname=models.CharField(max_length=100)
#item_id=models.PositiveIntegerField()
	


