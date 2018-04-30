from django.db import models
from django.contrib.auth.models import User


#from django.contrib.auth.models import User
class stock(models.Model):
	user= models.ForeignKey(User,on_delete=models.CASCADE)
	itemstock=models.PositiveIntegerField()
	itemcost=models.PositiveIntegerField()
	itemname=models.CharField(max_length=100)
#item_id=models.PositiveIntegerField()
	


