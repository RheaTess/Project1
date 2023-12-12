from django.db import models
from AdminApp.models import *

# Create your models here.
class Register(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField()
    PhNo=models.IntegerField()
    Password=models.CharField(max_length=30)

class Feedback(models.Model):
    Name=models.CharField(max_length=30)
    PhNo=models.IntegerField()
    Message=models.CharField(max_length=300)

class BookingForm(models.Model):
    LName=models.CharField(max_length=30)
    FName=models.CharField(max_length=30)
    userid=models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    serviceid=models.ForeignKey(Services,on_delete=models.CASCADE,null=True)
    Address1=models.CharField(max_length=30)
    Address2=models.CharField(max_length=30)
    Address3=models.CharField(max_length=30)
    # Service=models.CharField(max_length=60,default="")
    Date=models.CharField(max_length=100,default='')
    


    
